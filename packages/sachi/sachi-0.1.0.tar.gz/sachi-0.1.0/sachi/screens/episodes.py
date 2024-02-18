from typing import cast

from textual import on, work
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.screen import ModalScreen, Screen
from textual.widgets import (
    DataTable,
    Footer,
    Header,
    Input,
    Label,
    ListItem,
    ListView,
    Select,
    SelectionList,
)

from sachi.models import SachiMatch
from sachi.screens.rename import RenameScreen
from sachi.sources import SOURCE_CLASSES
from sachi.sources.base import SachiEpisodeModel, SachiParentModel, SachiSource


class ParentSelectionModal(ModalScreen[SachiParentModel]):
    def __init__(self, parents: list[SachiParentModel], **kwargs):
        super().__init__(**kwargs)
        self.parents = parents

    def compose(self) -> ComposeResult:
        with ListView():
            for parent in self.parents:
                yield ListItem(Label(f"{parent.title} ({parent.year})"))

    @on(ListView.Selected)
    async def select(self, event: ListView.Selected):
        assert event.list_view.index is not None
        self.dismiss(self.parents[event.list_view.index])


class EpisodesScreen(Screen):
    SUB_TITLE = "Episodes"
    CSS_PATH = __file__.replace(".py", ".tcss")
    BINDINGS = [
        ("a", "append_selection", "Append Selection"),
        ("r", "replace_selection", "Replace Selection"),
    ]

    sachi_source: reactive[SachiSource | None] = reactive(None)
    sachi_parent: reactive[SachiParentModel | None] = reactive(None)
    sachi_episodes: reactive[list[SachiEpisodeModel]] = reactive([])

    @property
    def selected_episodes(self) -> list[SachiEpisodeModel]:
        sel_list = self.query_one(SelectionList[int])
        episodes = [self.sachi_episodes[i] for i in sel_list.selected]
        return episodes

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            with Horizontal():
                yield Input(placeholder="Search", id="search-input", restrict=r".+")
                yield Select(
                    ((f"{s.service} ({s.media_type})", s) for s in SOURCE_CLASSES),
                    prompt="Source",
                )
            yield SelectionList[int](id="episodes-list")
        yield Footer()

    # Methods

    def deselect_all(self):
        sel_list = self.query_one(SelectionList[int])
        sel_list.deselect_all()

    # Event handlers

    @work
    @on(Input.Submitted, "#search-input")
    async def search(self, event: Input.Submitted):
        select = self.query_one(Select[type[SachiSource]])
        if not isinstance(select.value, type):
            return

        self.sachi_source = select.value.get_instance()
        parents = await self.sachi_source.search(event.value)
        self.sachi_parent = await self.app.push_screen_wait(
            ParentSelectionModal(parents)
        )

        self.sachi_episodes = await self.sachi_source.get_episodes(self.sachi_parent)

        sel_list = self.query_one(SelectionList[int])
        sel_list.clear_options()
        sel_list.add_options(
            (
                f"{self.sachi_parent.title} ({self.sachi_parent.year}) "
                f"- {ep.season:02}x{ep.episode:02} - {ep.name}",
                i,
            )
            for i, ep in enumerate(self.sachi_episodes)
        )

    @on(SelectionList.SelectedChanged, "#episodes-list")
    def on_episode_selected(self, event: SelectionList.SelectedChanged):
        event.control.action_cursor_down()

    # Key bindings

    def action_append_selection(self):
        if self.sachi_parent is None:
            return
        parent = self.sachi_parent
        screen = cast(RenameScreen, self.app.get_screen("rename"))
        table = screen.query_one(DataTable)
        j = 0
        for row in table.ordered_rows:
            if j >= len(self.selected_episodes):
                break
            file = screen.files[row.key]
            if file.match is None:
                file.match = SachiMatch(
                    parent=parent, episode=self.selected_episodes[j]
                )
                j += 1
        self.app.switch_screen("rename")
        self.deselect_all()

    def action_replace_selection(self):
        if self.sachi_parent is None:
            return
        parent = self.sachi_parent
        screen = cast(RenameScreen, self.app.get_screen("rename"))
        table = screen.query_one(DataTable)
        for row, ep in zip(table.ordered_rows, self.selected_episodes):
            screen.files[row.key].match = SachiMatch(parent=parent, episode=ep)
        self.app.switch_screen("rename")
        self.deselect_all()
