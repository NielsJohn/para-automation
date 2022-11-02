import streamlit as st

from directories import Paths, list_directories

paths = Paths('Documents/Para')

option = st.selectbox(label='PARA Folders', options=list_directories(paths.base))

st.write("You selected:", option)