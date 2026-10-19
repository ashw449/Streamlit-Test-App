import streamlit as st
st.title("Streamlit Test App")
st.write("This is a test app on streamlit")
name = st.text_input("Enter Your Name")
if name:
    st.write(f"Hello, {name}!")
else:
    st.warning("Please Enter your name.")