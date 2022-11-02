import streamlit as st
from tasks import archive_folder_ui, display_contents_ui

st.markdown("# Welcome to PARA!")

task_list = [
    "Display and open files and directories",
    "Archive a folder",
    "Move a folder",
    "Remove a folder",
]
task = st.radio("What do you want to do?", task_list)


if task == "Archive a folder":
    archive_folder_ui()
elif task == "Display and open files and directories":
    display_contents_ui()


