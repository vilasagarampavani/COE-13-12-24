import streamlit as st
st.title("Even or Odd")
num1 = st.number_input("enter number", min_value = 1, step = 3)
if st.button("Even or Odd"):
    if num1%2==0:
        st.success("Even number")
    else:
        st.error("Odd")
