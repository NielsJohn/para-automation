import streamlit as st

from directories import list_directories, move_directory, list_files, Paths

PATHS = Paths("Documents/Para")


def archive_folder_ui():
    parent_path = PATHS.base
    parent_options = [f.name for f in list_directories(parent_path) if f.name != "Archive"]
    parent_name = st.selectbox(
        label="PARA Folders",
        options=parent_options,
    )

    child_path = parent_path / parent_name
    child_options = [f.name for f in list_directories(child_path)]
    child_name = st.selectbox(
        label=parent_name,
        options=child_options,
    )

    if parent_name is not None:
        result = st.button("Archive!")

        if result:
            directory = child_path / child_name
            target_path = PATHS.archive
            move_directory(directory=directory, target_path=target_path)


def display_contents_ui():
    parent_path = PATHS.base
    parent_options = [f.name for f in list_directories(parent_path)]
    parent_name = st.selectbox(
        label="PARA Folders",
        options=parent_options,
    )

    child_path = parent_path / parent_name
    child_dirs = [f.name for f in list_directories(child_path)]
    child_files = [f.name for f in list_files(child_path)]
    child_dirs.extend(child_files)
    child_name = st.selectbox(
        label=parent_name,
        options=child_dirs,
    )

    # if parent_name is not None:
    #     result = st.button("Archive!")
    #
    #     if result:
    #         directory = child_path / child_name
    #         target_path = paths.archive
    #         move_directory(directory=directory, target_path=target_path)
