import streamlit as st
import streamlit.components.v1 as components
from streamlit_local_storage import LocalStorage

from openai import OpenAI
ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

local_storage = LocalStorage()

st.set_page_config(
    page_title="AI Task Manager",
    layout="wide"
)

st.title("AI Task Manager")
st.write("해야 할 일을 기록하고 관리합니다.")
st.title("AI Task Manager")

task = st.text_input(
    "해야 할 일을 입력하세요",
    placeholder="예: OpenAI API 연결하기"
)

if st.button("추가"):
    if task:
        st.success(f"추가됨: {task}")
    else:
        st.warning("할 일을 입력해주세요.")
