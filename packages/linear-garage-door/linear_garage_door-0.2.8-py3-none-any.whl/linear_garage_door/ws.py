from __future__ import annotations

import asyncio
from random import uniform
from typing import Any, Awaitable, Callable

from aiohttp import ClientSession, ClientWebSocketResponse, WSMsgType
from tenacity import retry, stop_after_attempt, wait_fixed

from ._util import parse_response
from .const import SERVICE_URL


async def cancel_task(*tasks: asyncio.Task[Any] | None) -> None:
    for task in tasks:
        if task is not None and not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass


class WebSocketMonitor:
    def __init__(self) -> None:
        self._disconnect = False
        self._ws: ClientWebSocketResponse | None = None
        self._monitor_task: asyncio.Task[Any] | None = None
        self._receiver_task: asyncio.Task[Any] | None = None
        self._callback: Callable[[dict[str, Any]], Awaitable[None]] | None = None
        self._session: ClientSession

    @property
    def connected(self) -> bool:
        if self._disconnect:
            return False
        return False if self._ws is None else not self._ws.closed

    @property
    def websocket(self) -> ClientWebSocketResponse | None:
        return self._ws

    @property
    def monitor(self) -> asyncio.Task[Any] | None:
        return self._monitor_task

    @retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
    async def new_connection(
        self,
        session: ClientSession,
        callback: Callable[[dict[str, Any]], Awaitable[None]] | None = None,
        start_monitor: bool = False,
        custom_session: bool = False,
    ) -> None:
        await cancel_task(self._receiver_task)
        self._disconnect = False
        self._ws = await session.ws_connect(SERVICE_URL, ssl=False)
        self._receiver_task = asyncio.ensure_future(self._receiver())
        self._callback = callback
        self._session = session
        self._custom_session = custom_session
        if start_monitor:
            await self.start_monitor()

    async def _receiver(self) -> None:
        if not (websocket := self._ws):
            return
        while not websocket.closed:
            msg = await websocket.receive()
            if msg.type in (WSMsgType.CLOSE, WSMsgType.CLOSING, WSMsgType.CLOSED):
                break

            if msg.type == WSMsgType.TEXT:
                response = parse_response(msg.data)
                if self._callback is not None:
                    await self._callback(response)

    async def _monitor(self) -> None:
        attempt = 0
        while not self._disconnect:
            while self.connected:
                await asyncio.sleep(1)
            if not self._disconnect:
                await self.new_connection(self._session, self._callback)
            if not self._ws or self._ws.closed:
                await asyncio.sleep(min(1 * 2**attempt + uniform(0, 1), 300))
                attempt += 1
                continue
            attempt = 0

    async def start_monitor(self) -> None:
        if self._monitor_task is None or self._monitor_task.done():
            self._monitor_task = asyncio.ensure_future(self._monitor())

    async def stop_monitor(self) -> None:
        await cancel_task(self._monitor_task)

    async def close(self) -> None:
        self._disconnect = True
        if self._ws:
            await self._ws.close()
            if not self._custom_session:
                await self._session.close()
        await cancel_task(self._monitor_task, self._receiver_task)
