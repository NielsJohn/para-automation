import shutil
from dataclasses import dataclass
from pathlib import Path

from settings import settings


@dataclass
class ParaPaths:
    """
    A class to manage the paths to your para folders.
    """

    def __post_init__(self) -> None:
        """
        Check if PARA folders exist. If not, create them in the home directory.
        Returns:
            None
        """
        initialize_folders(self.base)

    #TODO make this nice!
    @property
    def base(self) -> Path:
        return Path.cwd().parent.parent / 'data' / "PARA"

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

    @property
    def inbox(self) -> Path:
        return self.base / "Inbox"


def initialize_folders(base_dir: Path) -> None:
    """
    Create the folders to start with the PARA workflow.
    Args:
        base_dir: the directory of your PARA folders will be placed in.

    Returns:
        None
    """
    # create base folder
    if not base_dir.is_dir():
        base_dir.mkdir()

    # create subfolders
    for folder in settings.para_folders:
        if not (base_dir / folder).is_dir():
            (base_dir / folder).mkdir()


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
