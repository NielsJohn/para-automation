import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Paths:
    para_dir: str
    _base: Path = None

    @property
    def base(self) -> Path:
        if self._base is None:
            self._base = Path.home() / self.para_dir
        return self._base

    @property
    def projects(self) -> Path:
        return self.base / "Projects"

    @property
    def resources(self) -> Path:
        return self.base / "Resources"

    @property
    def areas(self) -> Path:
        return self.base / "Areas"

    @property
    def archive(self) -> Path:
        return self.base / "Archive"


def list_directories(source_path: Path) -> list[Path]:
    """
    List all the directories for a given source folder.
    Args:
        source_path: a path to a local directory.

    Returns:
        All directories in the source folder as pathlib objects.
    """
    return [f for f in source_path.iterdir() if f.is_dir()]


def list_files(source_path: Path) -> list[Path]:
    """
    List all the files for a given source folder.
    Args:
        source_path: a path to a local directory.

    Returns:
        All files in the source folder as pathlib objects.
    """
    return [f for f in source_path.iterdir() if f.is_file()]


def move_directory(directory: Path, target_path: Path) -> None:
    """
    Move a directory from a source path to a target path.
    Args:
        directory: the path to the directory
        target_path: the new path of the directory

    Returns:
        None
    """
    shutil.move(src=str(directory), dst=str(target_path))


def remove_directory(directory: Path) -> None:
    """
    Remove a directory
    Args:
        directory: the directory that will be removed.

    Returns:
        None
    """
    directory.rmdir()


if __name__ == "__main__":
    paths = Paths("Documents/Para")
