from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

from aiohttp import ClientSession

from hartware_lib.serializers.builders import DeserializerBuilder, SerializerBuilder
from hartware_lib.settings import HttpRpcSettings
from hartware_lib.types import AnyDict, Deserializer, Serializer

logger = logging.getLogger("hartware_lib.http_rpc_caller")


@dataclass
class HttpRpcCaller:
    settings: HttpRpcSettings
    serializer: Serializer
    deserializer: Deserializer

    @classmethod
    def build(
        cls,
        settings: HttpRpcSettings,
        serializer: Serializer = SerializerBuilder().get(),
        deserializer: Deserializer = DeserializerBuilder().get(),
    ) -> HttpRpcCaller:
        return cls(settings, serializer, deserializer)

    async def _process(self, data: AnyDict) -> Any:
        async with ClientSession() as session:
            response = await session.post(
                f"http://{self.settings.host}:{self.settings.port}/",
                data={"order": self.serializer(data).decode("utf-8")},
            )

            text = await response.text()

        data = self.deserializer(text)
        error = data.get("error")

        logger.info(f"received {len(text)} bytes ({type(data).__name__})")

        if error:
            raise Exception(f"{error}")

        return data.get("result")

    async def ping(self) -> bool:
        logger.info("ping")

        result = await self._process({"ping": True})

        if result.get("pong") is True:
            logger.info("pong received")

            return True

        raise Exception("No pong received")

    async def get_property(self, name: str) -> Any:
        logger.info(f"get_property: {name}")

        return await self._process({"property": name})

    async def set_property(self, name: str, value: Any) -> None:
        logger.info(f"set_property: {name} to {value:r}")

        await self._process({"property": name, "property_set": value})

    async def call(self, func: str, *args: Any, **kwargs: Any) -> Any:
        logger.info(f"call: {str(func)} = *{args}, **{kwargs}")

        return await self._process({"func": func, "args": args, "kwargs": kwargs})
