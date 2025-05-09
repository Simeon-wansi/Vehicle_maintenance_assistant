import streamlit as st


st.title("My first app")
st.write("Here's our first attempt at using data to create a table")
name = st.text_input("Enter your name")
if name:
    st.write("Hello", name, "Nice to meet you")