import streamlit as st
st.title("welcome to my first app")
st.header("hello")
name=st.text_input("enter your name...")
if st.button("submit"):

    st.write("hello",name)
