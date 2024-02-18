from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import StrEnum
from typing import Self

import aiohttp


class MediaType(StrEnum):
    SERIES = "series"
    MOVIE = "movie"


@dataclass
class SachiParentModel[RefIdType]:
    media_type: MediaType
    refId: RefIdType
    title: str
    year: int | None = None


@dataclass
class SachiEpisodeModel[RefIdType]:
    refId: RefIdType
    season: int
    episode: int
    name: str | None = None


class SachiSource[RefIdType](ABC):
    media_type: MediaType
    service: str

    _session: aiohttp.ClientSession | None = None
    _instance: Self | None = None

    @property
    def session(self) -> aiohttp.ClientSession:
        if self._session is None:
            self._session = aiohttp.ClientSession(raise_for_status=True)
        return self._session

    @abstractmethod
    async def search(self, query: str) -> list[SachiParentModel[RefIdType]]:
        ...

    @abstractmethod
    async def get_episodes(
        self, parent: SachiParentModel[RefIdType]
    ) -> list[SachiEpisodeModel[RefIdType]]:
        ...

    @classmethod
    def get_instance(cls) -> Self:
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init_subclass__(cls, /, media_type: MediaType, service: str, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.media_type = media_type
        cls.service = service
