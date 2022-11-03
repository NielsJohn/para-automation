import streamlit as st

from tasks import task_factory

st.markdown("# Welcome to PARA!")

task_list = [
    # "Display and open files and directories",
    "Archive a folder",
    # "Move a folder",
    # "Remove a folder",
]

# let the user select an action
action = st.radio("What do you want to do?", task_list)
task = task_factory(action)

# run the selected task
task()
