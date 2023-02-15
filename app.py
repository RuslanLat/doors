import streamlit as st

with open('./index.html', 'r', encoding="utf-8") as f:
    html = f.read()

st.markdown(html, unsafe_allow_html=True)