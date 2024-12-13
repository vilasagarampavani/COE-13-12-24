import streamlit as st
st.title("prime or not")
num = st.number_input("Enter the number:",min_value=0,step =1)
flag = False
if st.button("prime or not"):
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                flag = True
                break
        if flag:
            st.success("nOt prime")
        else:
            st.success("is prime")
