from typing import Callable

import streamlit as st

from directories import list_directories, move_directory, list_files, Paths

PATHS = Paths("data")


def task_factory(task: str) -> Callable:
    """
    Return an instance of a task.
    Args:
        task: the name of the task.

    Returns:
        The callable that contains the dashboard logic.
    """
    if task == "Archive a folder":
        return archive_folder
    else:
        raise NotImplementedError("This task is not available.")


def archive_folder() -> None:
    parent_options = [
        f.name for f in list_directories(PATHS.base) if f.name != "Archive"
    ]
    parent_name = st.selectbox(
        label="PARA Folders",
        options=parent_options,
    )

    child_path = PATHS.base / parent_name
    child_name = st.selectbox(
        label=parent_name,
        options=[f.name for f in list_directories(child_path)],
    )

    if parent_name is not None:
        result = st.button("Archive!")

        if result:
            move_directory(
                directory=child_path / child_name,
                target_path=PATHS.archive / child_name,
            )


def display_contents() -> None:
    parent_options = [f.name for f in list_directories(PATHS.base)]
    parent_name = st.selectbox(
        label="PARA Folders",
        options=parent_options,
    )

    child_path = PATHS.base / parent_name
    child_dirs = [f.name for f in list_directories(child_path)]
    child_files = [f.name for f in list_files(child_path)]
    child_dirs.extend(child_files)
    child_name = st.selectbox(
        label=parent_name,
        options=child_dirs,
    )

    # if (child_path / child_name).is_dir():
    #     result = st.button("Archive!")
    #
    #     if result:
    #         directory = child_path / child_name
    #         target_path = paths.archive
    #         move_directory(directory=directory, target_path=target_path)
