import streamlit as st
project  = st.number_input('Enter the project score:')
internal = st.number_input('Enter the internal score:')
external = st.number_input('Enter the extrenal score:')
if st.button("CAlculate grade:"):
  if project >=50 and internal >=50 and external >=50 :
    total = ((70 * project)  + (10 * internal)  + (20 * external) )/ 100
    if total >90 :
       st.success('Grade = A')
    elif total >80 and total <90:
       st.success('Grade = B')
    elif total > 80 and total < 50:
       st.success('Grade = C')
  else :
    print('Failed')
    if project < 50 :
        st.success('u failed in intrnal and project:')
    if internal < 50 :
        st.success('u falied in internal and external')
    if external <50:
        st.success('u falied in project and external')


