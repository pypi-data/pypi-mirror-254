import asyncio
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Self, assert_never, cast

import jinja2
from guessit import guessit
from pymediainfo import MediaInfo
from rich.text import Text

from sachi.config import BaseConfig, read_config
from sachi.context import FileBotContext
from sachi.sources.base import (
    MediaType,
    SachiEpisodeModel,
    SachiParentModel,
)

FS_SPECIAL_CHARS = re.compile(r"[/\\:*\"?<>|]")


@dataclass
class SachiMatch:
    parent: SachiParentModel
    episode: SachiEpisodeModel


class SachiFile:
    def __init__(
        self, path: Path, base_dir: Path, set_rename_cell: Callable[[Any], None]
    ):
        self.path = path
        self.base_dir = base_dir
        self.set_rename_cell = set_rename_cell

        self._match: SachiMatch | None = None

        self.ctx = FileBotContext()
        self.analyze_filename()
        self.media_analysis_done = asyncio.Event()

        self.new_path = asyncio.Future[Path]()

    @property
    def match(self) -> SachiMatch | None:
        return self._match

    @match.setter
    def match(self, value: SachiMatch | None):
        self._match = value

        self.set_rename_cell(
            Text(
                f"{value.parent.title} ({value.parent.year}) "
                f"- {value.episode.season:02}x{value.episode.episode:02} "
                f"- {value.episode.name}",
                style="italic",
            )
            if value
            else None
        )

        self.analyze_match()

        if value is not None and not self.media_analysis_done.is_set():
            asyncio.create_task(asyncio.to_thread(self.analyze_media))

        if self.new_path.done():
            self.new_path = asyncio.Future[Path]()
        asyncio.create_task(self.template_new_path())

    def analyze_filename(self):
        guess = cast(dict, guessit(self.path.name))
        self.ctx.source = guess.get("source", None)

    def analyze_media(self):
        media_info = MediaInfo.parse(self.path)
        if isinstance(media_info, str):
            raise RuntimeError(f"Failed to parse media info: {media_info}")

        video = media_info.video_tracks[0]
        self.ctx.resolution = f"{video.width}x{video.height}"
        self.ctx.bitdepth = video.bit_depth
        self.ctx.vc = video.encoded_library_name

        audio = media_info.audio_tracks[0]
        self.ctx.ac = audio.format

        self.media_analysis_done.set()

    def analyze_match(self):
        if self.match is None:
            return
        parent, episode = self.match.parent, self.match.episode

        self.ctx.n = parent.title

        if episode is not None:
            self.ctx.s = episode.season
            self.ctx.s00e00 = f"S{episode.season:02}E{episode.episode:02}"
            self.ctx.t = episode.name

    async def template_new_path(self):
        if self.match is None:
            return

        await self.media_analysis_done.wait()

        config = read_config()
        config_model = BaseConfig(**config.unwrap())

        match self.match.parent.media_type:
            case MediaType.SERIES:
                template_list = config_model.series.template
            case MediaType.MOVIE:
                template_list = config_model.movie.template
            case _:
                assert_never(self.match.parent.media_type)

        new_path = self.base_dir
        ctx_dict = asdict(self.ctx)
        for part in template_list:
            template = jinja2.Template(part)
            segment = template.render(ctx_dict)
            segment = FS_SPECIAL_CHARS.sub("", segment)
            new_path /= segment
        new_path = new_path.with_suffix(self.path.suffix)
        self.set_rename_cell(str(new_path.relative_to(self.base_dir)))
        self.new_path.set_result(new_path)

    def __eq__(self, other: object):
        return isinstance(other, SachiFile) and self.path == other.path

    def __lt__(self, other: Self):
        return self.path < other.path

    def __le__(self, other: Self):
        return self.path <= other.path

    def __gt__(self, other: Self):
        return self.path > other.path

    def __ge__(self, other: Self):
        return self.path >= other.path
