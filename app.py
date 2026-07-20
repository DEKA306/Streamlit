import streamlit as st
st.title("카운터 앱")
if 'ct' not in st.session_state:
    st.session_state.ct = 0
if st.button("증가"):
    st.session_state.ct += 1
st.markdown(f"## 현재 숫자 : `{st.session_state.ct}`")
