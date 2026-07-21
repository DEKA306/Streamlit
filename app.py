import streamlit as st
import streamlit.components.v1 as components
from streamlit_local_storage import LocalStorage

from openai import OpenAI

ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

local_storage = LocalStorage()

st.title("AI Task Manager")

# 저장된 작업 가져오기
tasks = local_storage.getItem("tasks")

if tasks is None:
    tasks = []

# 입력
task = st.text_input(
    "앞으로 해야 할 일을 입력하세요",
    placeholder="여기에 입력해주세요. "
)

# 추가
if st.button("추가"):
    if task:
        tasks.append(task)
        local_storage.setItem("tasks", tasks)
        st.success("저장되었습니다.")
        st.rerun()
    else:
        st.warning("할 일을 입력해주세요.")

st.subheader("해야 할 일")

for i, t in enumerate(tasks):
    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(f"{i+1}. {t}")

    with col2:
        if st.button("제거", key=f"remove_{i}"):
            tasks.pop(i)
            local_storage.setItem("tasks", tasks)
            st.rerun()
