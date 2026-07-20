import streamlit as st

st.title("카운터 앱")
ct = 0
if st.button("증가"):
    ct == 1
st.markdown(f"## 현재 숫자 : `{ct}`")
