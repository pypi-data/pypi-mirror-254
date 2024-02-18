"""Asynchronous Python client for Cambridge Audio StreamMagic Devices."""
from __future__ import annotations

import asyncio
import socket
from dataclasses import dataclass
from importlib import metadata
from typing import Any, Optional, Type

import async_timeout
from aiohttp.client import ClientError, ClientResponseError, ClientSession
from aiohttp.hdrs import METH_GET
from yarl import URL

from .exceptions import StreamMagicConnectionError, StreamMagicError
from .models import Info, Source, State

@dataclass
class StreamMagic:
    """Main class for handling connections with a StreamMagic device."""

    def __init__(self, host: str, session: ClientSession | None=None) -> None:
        self._host = host
        self._request_timeout = 100
        self._close_session: bool = False
        self._session = session
        if session is None:
            self._session = ClientSession()
            self._close_session = True

    async def close(self) -> None:
        """Close open client session."""
        if self._session and self._close_session:
             await self._session.close()
        return await self._session.close()
        
    async def __aenter__(self) -> "StreamMagic":
        """Async enter.
        Returns:
            The StreamMagic object.
        """
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[async_timeout.TracebackType],
    ) -> Optional[bool]:
        await self.close()
        return None
    
    
    async def _request(self, path: str,
                       query: str = "",
                       method: str = METH_GET,
                       ) -> dict[str, Any]:
        """Handle a request to a StreamMagic device.
        A generic method for sending/handling HTTP requests done against
        the StreamMagic API.
        Args:

        Returns:
            
        Raises:
            
        """

        version = metadata.version(__package__)
        url = URL.build(
            scheme="http", host=self._host, path=path, query=query)

        headers = {
            "User-Agent": f"PythonAsyncStreamMagic/{version}",
            "Accept": "application/json, text/plain, */*",
        }

        try:
            async with async_timeout.timeout(self._request_timeout):
                response = await self._session.get(
                url,
                headers=headers,
                )
                response.raise_for_status()
        except asyncio.TimeoutError as exception:
            raise StreamMagicConnectionError(
                "Timeout occurred while connecting to Elgato Light device"
            ) from exception
        except (
            ClientError,
            ClientResponseError,
            socket.gaierror,
        ) as exception:
            raise StreamMagicConnectionError(
                {"Error occurred while communicating with StreamMagic device", exception}
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            text = await response.text()
            raise StreamMagicError(
                "Unexpected response from the StreamMagic device",
                {"Content-Type": content_type, "response": text},
            )
        await asyncio.sleep(0)
        return await response.json()

    async def get_info(self) -> Info:
        """Get devices information from StreamMagic device.
        Returns:
            A Info object, with information about the StreamMagic device.
        """
        data = await self._request(path="/smoip/system/info")
        return Info.parse_obj(data["data"])

    async def get_sources(self) -> list(Source):
        """Get source list from StreamMagic device.
        Returns:
            A Settings object, with information about the StreamMagic device.
        """
        request = await self._request(path="/smoip/system/sources")
        data = request["data"]["sources"]
        source_list = []
        for item in data:
            source_list.append(Source.parse_obj(item))
        return source_list

    async def get_state(self) -> State:
        """Get the current state of StreamMagic device.
        Returns:
            A State object, with the current StreamMagic device state.
        """
        data = await self._request(path="/smoip/zone/state", query="zone=ZONE1")
        return State.parse_obj(data["data"])

    async def set_power_on(self) -> None:
        """Set the power of StreamMagic device on."""
        await self._request(path="/smoip/zone/state", query="zone=ZONE1&power=true")

    async def set_power_off(self) -> None:
        """Set the power of StreamMagic device on."""
        await self._request(path="/smoip/zone/state", query="zone=ZONE1&power=false")

    async def set_volume_step_up(self) -> None:
        """Set the power of StreamMagic device on."""
        await self._request(path="/smoip/zone/state", query="zone=ZONE1&volume_step_change=1")

    async def set_volume_step_down(self) -> None:
        """Set the power of StreamMagic device on."""
        await self._request(path="/smoip/zone/state", query="zone=ZONE1&volume_step_change=-1")

    async def set_volume_percent(self, volume: int) -> None:
        """Set the power of StreamMagic device on."""
        if not 0 <= volume <= 100:
            raise StreamMagicError("Volume not between 0 and 100")
        query = "zone=ZONE1&volume_percent=" + str(volume)
        await self._request(path="/smoip/zone/state", query=query)

    async def set_volume_mute_on(self) -> None:
        """Set the power of StreamMagic device on."""
        await self._request(path="/smoip/zone/state", query="zone=ZONE1&mute=true")

    async def set_volume_mute_off(self) -> None:
        """Set the power of StreamMagic device on."""
        await self._request(path="/smoip/zone/state", query="zone=ZONE1&mute=false")

    async def set_source(self, source: Source) -> None:
        """Set the power of StreamMagic device on."""
        query = "zone=ZONE1&source=" + source.id
        await self._request(path="/smoip/zone/state", query=query)