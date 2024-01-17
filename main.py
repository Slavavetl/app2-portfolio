import streamlit as st
import pandas

st.set_page_config(layout="wide")

col0, col1, col2 = st.columns([1,3,4])

with col0:
    st.write("")

with col1:
    st.image("images/photo.png", width=250)

with col2:
    st.title("Slava V")
    content = """
    Hi, I am a learner to code in Python....
    Trying to elevate and engage my expertise in auditing and analytics with coding.  
    By profession I am...    
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.info(content2)

df = pandas.read_csv("data.csv", sep=';')

col3, empty_col, col4 = st.columns([6,1,6])

#with col3:
#    for index, row in df.iterrows():
#        if index % 2:
#            st.header(row['title'])
#
#with col4:
#    for index, row in df.iterrows():
#        if not index % 2:
#            st.header(row['title'])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[>> Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[>> Source code]({row['url']})")