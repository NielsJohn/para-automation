import streamlit as st

from settings import settings
from core.tasks import task_factory


st.markdown("# Welcome to PARA!")

# let the user select an action
action = st.radio("What do you want to do?", settings.TASK_LIST)
try:
    # get task from task factory
    task = task_factory(action)

    # run the selected task
    task()
except NotImplementedError:
    st.markdown("### This method is not implemented (yet).")
