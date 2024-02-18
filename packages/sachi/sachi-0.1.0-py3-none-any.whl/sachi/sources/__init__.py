from typing import TYPE_CHECKING

from sachi.sources.tvdb import TVDBSource

if TYPE_CHECKING:
    from sachi.sources.base import SachiSource


SOURCE_CLASSES: list[type["SachiSource"]] = [
    TVDBSource,
]
