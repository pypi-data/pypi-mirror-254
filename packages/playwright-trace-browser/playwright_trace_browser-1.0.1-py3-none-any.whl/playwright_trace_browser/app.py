import sys
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import var
from textual.widgets import DirectoryTree, Footer, Header

from playwright_trace_browser._folder import create_restructured_temp_dir_for_viewing
from playwright_trace_browser._viewer import open_trace_viewer


class PlaywrightTraceBrowser(App):
    """Textual Playwright trace browser app."""

    CSS_PATH = "app.tcss"
    BINDINGS = [
        ("f", "toggle_files", "Toggle Files"),
        ("q", "quit", "Quit"),
    ]

    show_tree = var(True)

    def watch_show_tree(self, show_tree: bool) -> None:
        """Called when show_tree is modified."""
        self.set_class(show_tree, "-show-tree")

    def compose(self) -> ComposeResult:
        """Compose our UI."""
        path = "./" if len(sys.argv) < 2 else sys.argv[1]
        temp_path = create_restructured_temp_dir_for_viewing(Path(path))
        yield Header()
        with Container():
            yield DirectoryTree(temp_path, id="tree-view")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(DirectoryTree).focus()

    async def on_directory_tree_file_selected(
        self, event: DirectoryTree.FileSelected
    ) -> None:
        """Called when the user click a file in the directory tree."""
        event.stop()
        # await open_trace_viewer(event.path)
        self.run_worker(self.open_trace_viewer(event.path))

    async def open_trace_viewer(self, path: Path) -> None:
        await open_trace_viewer(path)

    def action_toggle_files(self) -> None:
        """Called in response to key binding."""
        self.show_tree = not self.show_tree


if __name__ == "__main__":
    PlaywrightTraceBrowser().run()
