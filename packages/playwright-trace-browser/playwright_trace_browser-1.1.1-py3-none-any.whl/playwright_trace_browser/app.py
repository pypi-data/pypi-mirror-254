import sys
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import DirectoryTree, Footer, Header

from playwright_trace_browser._folder import create_restructured_temp_dir_for_viewing
from playwright_trace_browser._image import open_image
from playwright_trace_browser._viewer import open_trace_viewer

placeholder_image_path = Path(__file__).parent / "placeholder.jpg"


class PlaywrightTraceBrowser(App):
    """Textual Playwright trace browser app."""

    CSS_PATH = "app.tcss"
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def __init__(self) -> None:
        super().__init__()
        path = "./" if len(sys.argv) < 2 else sys.argv[1]
        self.path = create_restructured_temp_dir_for_viewing(Path(path))

    def compose(self) -> ComposeResult:
        """Compose our UI."""
        yield Header()
        with Container():
            yield DirectoryTree(self.path, id="tree-view")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(DirectoryTree).focus()

    async def on_directory_tree_file_selected(
        self, event: DirectoryTree.FileSelected
    ) -> None:
        """Called when the user click a file in the directory tree."""
        event.stop()
        if event.path.suffix == ".zip":
            self.run_worker(self.open_trace_viewer(event.path))
        else:
            self.run_worker(self.open_image(event.path))

    async def open_trace_viewer(self, path: Path) -> None:
        await open_trace_viewer(path)

    async def open_image(self, path: Path) -> None:
        await open_image(path)


if __name__ == "__main__":
    PlaywrightTraceBrowser().run()
