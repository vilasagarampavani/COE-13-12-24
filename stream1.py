import streamlit as st
st.title("multiples of 100 or not")
num1 = st.number_input("enter number")
if st.button("multiples of 100 or not"):
    if num1%100==0:
        st.success("multiple of 100")
    else:
        st.error("not a multiple of 100 ")
