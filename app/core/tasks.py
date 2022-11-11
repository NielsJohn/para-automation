from typing import Callable

import streamlit as st

from core.dir_manipulation import (
    list_directories,
    move_directory,
    ParaPaths,
    remove_directory,
)

PATHS = ParaPaths()


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
    elif task == "Display contents":
        return display_contents
    elif task == "Move a folder":
        return move_folder
    elif task == "Remove a folder":
        return remove_folder
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

    if child_name is not None:
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
    st.selectbox(label="Folders", options=child_dirs)


def move_folder() -> None:
    st.markdown("### Source")
    parent_options = [f.name for f in list_directories(PATHS.base)]
    parent_name = st.selectbox(
        label="PARA Folders",
        options=parent_options,
    )

    child_path = PATHS.base / parent_name
    child_dirs = [f.name for f in list_directories(child_path)]
    child_name = st.selectbox(
        label=parent_name,
        options=child_dirs,
    )

    if (child_path / child_name).is_dir():
        st.markdown("### Destination")
        target_options = [f.name for f in list_directories(PATHS.base)]
        target_name = st.selectbox(label="PARA Folders", options=target_options, key=2)

        if target_name is not None:
            result = st.button("Move!")

            if result:
                move_directory(
                    directory=child_path / child_name,
                    target_path=PATHS.base / target_name / child_name,
                )


def remove_folder() -> None:
    parent_options = [f.name for f in list_directories(PATHS.base)]
    parent_name = st.selectbox(
        label="PARA Folders",
        options=parent_options,
    )

    child_path = PATHS.base / parent_name
    child_name = st.selectbox(
        label=parent_name,
        options=[f.name for f in list_directories(child_path)],
    )

    if child_name is not None:
        result = st.button("Remove!")

        if result:
            remove_directory(
                directory=child_path / child_name,
            )
