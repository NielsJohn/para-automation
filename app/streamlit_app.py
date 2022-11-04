import streamlit as st

from app.core.tasks import task_factory
from app.settings import settings

st.markdown("# Welcome to PARA!")

# let the user select an action
action = st.radio("What do you want to do?", settings.task_list)
task = task_factory(action)

# run the selected task
task()
