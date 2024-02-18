from contextlib import suppress
from functools import partial
from pathlib import Path
from typing import Generator, Literal, assert_never

from textual.app import ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import DataTable, Footer, Header
from textual.widgets.data_table import CellDoesNotExist, RowKey

from sachi.models import SachiFile


class RenameScreen(Screen):
    SUB_TITLE = "Rename"
    CSS_PATH = __file__.replace(".py", ".tcss")
    BINDINGS = [
        ("j", "move('down')", "Move Down"),
        ("k", "move('up')", "Move Up"),
        ("d", "remove_element", "Remove"),
        ("p", "apply_renames", "Apply"),
    ]

    files: reactive[dict[RowKey, SachiFile]] = reactive({})

    def __init__(self, file_or_dir: Path, **kwargs):
        super().__init__(**kwargs)
        self.file_or_dir = file_or_dir
        self.base_dir = file_or_dir.parent if file_or_dir.is_file() else file_or_dir

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(zebra_stripes=True)
        yield Footer()

    # Methods

    def iter_files(self, file_or_dir: Path) -> Generator[Path, None, None]:
        if file_or_dir.name.startswith("."):
            return
        if file_or_dir.is_file():
            yield file_or_dir
        elif file_or_dir.is_dir():
            for file in file_or_dir.iterdir():
                yield from self.iter_files(file)
        else:
            raise RuntimeError(f"Invalid file or directory: {file_or_dir}")

    # Event handlers

    async def on_mount(self):
        table = self.query_one(DataTable)
        col_keys = table.add_columns("From", "To")
        for path in self.iter_files(self.file_or_dir):
            row_key = table.add_row(
                str(path.relative_to(self.base_dir)),
                None,
            )
            self.files[row_key] = SachiFile(
                path,
                self.base_dir,
                partial(table.update_cell, row_key, col_keys[1], update_width=True),
            )
        table.sort(col_keys[0])
        table.focus()

    # Key bindings

    def action_move(self, direction: Literal["up", "down"]):
        with suppress(CellDoesNotExist):
            table = self.query_one(DataTable)

            cood = table.cursor_coordinate
            cell_key = table.coordinate_to_cell_key(cood)

            match direction:
                case "up":
                    cood_other = cood.up()
                case "down":
                    cood_other = cood.down()
                case _:
                    assert_never(direction)
            cell_other_key = table.coordinate_to_cell_key(cood_other)

            col_i = table.cursor_column
            file = self.files[cell_key.row_key]
            file_other = self.files[cell_other_key.row_key]
            if col_i == 0:
                self.files[cell_key.row_key], self.files[cell_other_key.row_key] = (
                    file_other,
                    file,
                )
                file.set_rename_cell, file_other.set_rename_cell = (
                    file_other.set_rename_cell,
                    file.set_rename_cell,
                )
                table.update_cell_at(
                    cood_other,
                    str(file.path.relative_to(self.base_dir)),
                )
                table.update_cell_at(
                    cood,
                    str(file_other.path.relative_to(self.base_dir)),
                )
            file_other.match, file.match = file.match, file_other.match

            match direction:
                case "up":
                    table.action_cursor_up()
                case "down":
                    table.action_cursor_down()
                case _:
                    assert_never(direction)

    def action_remove_element(self):
        table = self.query_one(DataTable)
        cell_key = table.coordinate_to_cell_key(table.cursor_coordinate)
        col_i = table.cursor_column
        match col_i:
            case 0:
                table.remove_row(cell_key.row_key)
                del self.files[cell_key.row_key]
            case 1:
                self.files[cell_key.row_key].match = None
            case _:
                raise RuntimeError(f"Invalid column: {col_i}")

    async def action_apply_renames(self):
        table = self.query_one(DataTable)
        for row in table.ordered_rows:
            file = self.files[row.key]

            if file.match is not None:
                new_path = await file.new_path
                new_path.parent.mkdir(parents=True, exist_ok=True)
                file.path.rename(new_path)

                table.remove_row(row.key)
                del self.files[row.key]
