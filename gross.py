import streamlit as st
st.title("Gross Salary")
Basic = st.number_input('Ehter the salary:',min_value=0,step=1)
if st.button(" calculate Gross Salary"):
    HRA =0
    DA =0
    if Basic  < 10000:
         HRA = (67 *Basic)/100
         DA = (67 *Basic)/100
    elif Basic > 10000 and Basic <20000 :
         HRA = (69*Basic)/100
         DA = (76*Basic)/100
    elif Basic > 20000:
         HRA = (73*Basic)/100
         DA = (89*Basic)/100
    st.write("HRA:",HRA)
    st.write("DA:",DA)
    GS = HRA +  DA + Basic
    st.write("GS:",GS)