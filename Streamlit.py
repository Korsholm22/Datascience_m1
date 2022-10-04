import streamlit as st 

st.title("Hello")
st.write("Hello App!")

tabs1, tabs2 = (["Tab1, tab2"])

with tabs1:
    st.header("Hello")

with tabs2:
    st.header("Hello2")
