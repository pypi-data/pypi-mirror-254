import asyncio
import base64
import pprint
from collections.abc import Callable
from enum import Enum
from typing import Any, Self, Iterable

import aiohttp
import async_timeout
from aiohttp import WSMsgType

from .const import LOGGER
from .metadata_pb2 import DeviceMetadata
from .pubsub_pb2 import (
    CommandRequestData,
    CommandReplyData,
    CommandRequest,
    REQUEST_TYPE_DATA,
    CommandReply,
    REPLY_TYPE_ERROR,
)
from .reports_pb2 import GatewayReport
from .websocket_pb2 import WebsocketMessage

CONNECT_ERRORS = (
    aiohttp.ClientError,
    asyncio.TimeoutError,
    OSError,
)


class DeviceInfo:
    def __init__(self, mac, typ, revision):
        self.mac = mac
        self.type = typ
        self.revision = revision

    @classmethod
    def from_dict(cls, json: dict[str, Any]) -> Self:
        return cls(
            json["mac"],
            json["type"],
            json["revision"],
        )


class DeviceNode:
    def __init__(self, uuid: bytes, capabilities: Iterable[str]):
        self.uuid = uuid
        self.capabilities = capabilities

    @classmethod
    def from_dict(cls, json: dict[str, Any]) -> Self:
        return cls(
            base64.b64decode(json["UUID"]),
            json["Capabilities"],
        )


class DeviceConnectionError(Exception):
    pass


class Event(Enum):
    CONN_CLOSED = 1


class Client:
    message_handler: Callable[[GatewayReport], None]
    event_handler: Callable[[Event], None]

    def __init__(self, host: str, port: int, session: aiohttp.ClientSession):
        self.host = host
        self.port = port
        self.session = session
        self._calls: dict[int, Call] = {}
        self._call_id = 0

    async def get_info(self) -> DeviceInfo:
        try:
            async with self.session.get(
                    f"http://{self.host}:{self.port}/api/v1/settings/structure",
                    raise_for_status=True,
                    timeout=10,
            ) as resp:
                return DeviceInfo.from_dict(await resp.json())
        except CONNECT_ERRORS as err:
            raise DeviceConnectionError(err) from err

    async def get_nodes(self) -> Iterable[DeviceNode]:
        try:
            async with self.session.get(
                    f"http://{self.host}:{self.port}/api/v1/settings/nodes",
                    raise_for_status=True,
                    timeout=10,
            ) as resp:
                json = await resp.json()
                return [DeviceNode.from_dict(c) for c in json["Capabilities"]]
        except CONNECT_ERRORS as err:
            raise DeviceConnectionError(err) from err

    async def turn_on(self, device_id: bytes) -> None:
        data = CommandRequestData()
        data.SwitchOn.metadata.CopyFrom(metadata(device_id))
        await self._call("Switch/SwitchOn", data)

    async def turn_off(self, device_id: bytes) -> None:
        data = CommandRequestData()
        data.SwitchOff.metadata.CopyFrom(metadata(device_id))
        await self._call("Switch/SwitchOff", data)

    async def connect(self):
        LOGGER.debug("Trying to connect to device at %s", self.host)
        self._client = await self.session.ws_connect(
            f"http://{self.host}:{self.port}/rpc", autoping=False
        )
        self._rx_task = asyncio.create_task(self._rx_msgs())
        LOGGER.debug("Connected to %s", self.host)

    async def _rx_msgs(self) -> None:
        while not self._client.closed:
            msg = await self._client.receive()
            LOGGER.debug("Received msg (%s): %s", self.host, msg)
            LOGGER.debug("MSG type %s : %s", msg.type, msg.type == WSMsgType.CLOSED)
            if msg.type == WSMsgType.CLOSED:
                LOGGER.debug("MSG TYPE CLOSED")
                break
            m = WebsocketMessage()
            m.ParseFromString(msg.data)

            pp = pprint.PrettyPrinter(indent=4)
            LOGGER.debug("MSG: %s", pp.pformat(m))

            if not self._client.closed:
                if m.frame_id > 0:
                    if m.frame_id not in self._calls:
                        LOGGER.warning("Response for an unknown request id: %s", m.frame_id)
                        return
                    call = self._calls.pop(m.frame_id)
                    if not call.resolve.cancelled():
                        call.resolve.set_result(m.reply)
                else:
                    LOGGER.debug("Handle report")
                    if self.message_handler:
                        self.message_handler(m.gateway_report)

        LOGGER.debug("Websocket client connection from %s closed", self.host)

        for call_item in self._calls.values():
            if not call_item.resolve.done():
                call_item.resolve.set_exception(Exception())
        self._calls.clear()

        if not self._client.closed:
            await self._client.close()

        self._client = None
        self.event_handler(Event.CONN_CLOSED)

    async def close(self):
        if self._rx_task:
            self._rx_task.cancel()
        if self._client:
            await self._client.close()

    async def _call(self, method: str, data: CommandRequestData, timeout: int = 10) -> CommandReplyData:
        call = Call(self._next_id, method, data)
        self._calls[call.frame_id] = call
        try:
            async with async_timeout.timeout(timeout):
                await call.send_request(self)
                reply: CommandReply = await call.resolve
        except asyncio.TimeoutError as exc:
            call.resolve.cancel()
            await call.resolve
            raise exc
        except ConnectionResetError as exc:
            raise exc

        if reply.type == REPLY_TYPE_ERROR:
            raise Exception(reply.error.message)

        return reply.data

    @property
    def _next_id(self) -> int:
        self._call_id += 1
        return self._call_id

    async def send_bytes(self, data: bytes):
        if self._client is None:
            raise RuntimeError("Not connected")
        await self._client.send_bytes(data)


class Call:
    def __init__(self, frame_id, method: str, data: CommandRequestData) -> None:
        self.frame_id = frame_id
        self.method = method
        self.data = data
        self.resolve: asyncio.Future = asyncio.Future()

    async def send_request(self, client: Client):
        req = CommandRequest()
        req.method = self.method
        req.type = REQUEST_TYPE_DATA
        req.data.CopyFrom(self.data)
        msg = WebsocketMessage()
        msg.frame_id = self.frame_id
        msg.request.CopyFrom(req)
        await client.send_bytes(msg.SerializeToString())


def metadata(device_id: bytes) -> DeviceMetadata:
    meta = DeviceMetadata()
    meta.mqtt.device_id = device_id
    return meta
