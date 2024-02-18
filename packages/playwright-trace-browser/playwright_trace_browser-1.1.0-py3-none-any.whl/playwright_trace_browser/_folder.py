from __future__ import annotations

import os
import shutil
import tempfile
from dataclasses import dataclass, replace
from functools import cached_property
from pathlib import Path
from typing import Sequence

import more_itertools


@dataclass(frozen=True)
class _File:
    path: Path
    original_path: Path


@dataclass(frozen=True)
class _FileTree:
    path: Path
    children: "Sequence[_File | _FileTree]"

    @cached_property
    def common_base_path_str(self) -> str:
        """Return the common base path of all files."""
        if not self.children:
            return ""
        folders = set(file.path.parent for file in self.children)
        if len(folders) == 1:
            # Cannot have common if there is only one folder
            return ""
        return os.path.commonprefix([str(folder.name) for folder in folders])

    @cached_property
    def files(self) -> list[_File]:
        files: list[_File] = []
        for child in self.children:
            if isinstance(child, _File):
                files.append(child)
            elif isinstance(child, _FileTree):
                files.extend(child.files)
            else:
                raise ValueError(f"Unknown type: {child}")
        return files

    def with_base_path_folder(self, base_path_str: str | None = None) -> "_FileTree":
        common_base_path_str = base_path_str or self.common_base_path_str
        common_base_path = Path(common_base_path_str.rstrip("-"))

        def transform_path(p: Path) -> Path:
            parent_folder_name = p.parent.name
            parent_folder_without_common_base_path = parent_folder_name[
                len(common_base_path_str) :
            ]
            return (
                p.parent.parent
                / common_base_path
                / parent_folder_without_common_base_path
                / p.name
            )

        return self.__class__(
            path=self.path / common_base_path,
            children=[
                _File(path=transform_path(f.path), original_path=f.original_path)
                for f in self.files
            ],
        )

    def common_base_names(self) -> list[str]:
        common_base_paths = []
        for file1, file2 in more_itertools.windowed(self.files, 2):
            if file1 is None or file2 is None:
                continue
            file_list = self.__class__(path=self.path, children=[file1, file2])
            common_base_paths.append(file_list.common_base_path_str)
        return [p for p in common_base_paths if p]

    @classmethod
    def from_paths(
        cls, paths: list[Path], parent_path: Path = Path(".")
    ) -> "_FileTree":
        all_files: list[_File | _FileTree] = [
            _File(path=p, original_path=p) for p in sorted(paths, key=lambda p: str(p))
        ]
        obj = cls(path=parent_path, children=all_files)
        return obj.restructure_files_into_tree()

    def restructure_files_into_tree(self) -> "_FileTree":
        obj = replace(self)
        cls = self.__class__

        # Handle top level of tree
        common_base_names = self.common_base_names()
        if os.path.commonprefix(common_base_names):
            # There is a single common base path to create
            obj = cls(path=obj.path, children=[obj.with_base_path_folder()])
        elif common_base_names:
            # There are multiple common base paths to create
            unique_common_base_paths = set([bp for bp in common_base_names if bp])
            # Gather the files that have the same common base path
            children: list[_File | _FileTree] = []
            for base_path in unique_common_base_paths:
                files_for_base_path = [
                    f
                    for f in obj.files
                    if str(f.path.parent.name).startswith(base_path)
                ]
                file_tree = cls(
                    path=obj.path, children=files_for_base_path
                ).with_base_path_folder()
                children.append(file_tree)
            obj = replace(obj, children=children)

        # Recurse into the children
        new_children: list[_File | _FileTree] = []
        for child in obj.children:
            if isinstance(child, _FileTree):
                new_children.append(child.restructure_files_into_tree())
            else:
                new_children.append(child)
        obj = replace(obj, children=new_children)

        return obj

    def copy_from_originals(self, input_folder: Path):
        for file in self.files:
            full_path = self.path / file.path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(input_folder / file.original_path, full_path)


def create_restructed_folder_for_viewing(in_folder: Path, out_folder: Path):
    """
    Create a restructured folder for viewing Playwright traces.

    Playwright trace folders can get very long and common names, such as:
    - e2e-my-dir-my-subdir-test-one
        - test-failed-1.png
        - trace.zip
    - e2e-my-dir-my-subdir-test-two
        - test-failed-1.png
        - trace.zip
    - e2e-my-dir-subdir2-test-one
        - test-failed-1.png
        - trace.zip
    - e2e-my-dir-subdir2-test-two
        - test-failed-1.png
        - trace.zip

    Restructure this into a nested heirarchy of folders that does not repeat path parts:
    - e2e-my-dir
        - my-subdir-test
            - one
                - test-failed-1.png
                - trace.zip
            - two
                - test-failed-1.png
                - trace.zip
        - subdir2-test
            - one
                - test-failed-1.png
                - trace.zip
            - two
                - test-failed-1.png
                - trace.zip
    """
    # Create the out folder if it does not exist
    out_folder.mkdir(exist_ok=True)

    # Get all the trace folders
    all_paths = list(in_folder.glob("**/*"))
    all_files = [f.relative_to(in_folder) for f in all_paths if f.is_file()]
    file_tree = _FileTree.from_paths(all_files, parent_path=out_folder)
    file_tree.copy_from_originals(in_folder)


def create_restructured_temp_dir_for_viewing(in_folder: Path) -> Path:
    out_folder = Path(tempfile.TemporaryDirectory().name)
    create_restructed_folder_for_viewing(in_folder, out_folder)
    return out_folder


if __name__ == "__main__":
    input_folder = Path(__file__).parent.parent / "sample-traces"
    output_folder = Path(__file__).parent.parent / "sample-traces-restructured"
    create_restructed_folder_for_viewing(input_folder, output_folder)
