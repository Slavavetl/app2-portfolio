import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=200)

with col2:
    st.title("Slava V")
    content = """
    Hi, I am a learner to code in Python....
    Trying to elevate and engage my expertise in auditing and analytics with coding.  
    By profession I am...    
    """
    st.info(content)

