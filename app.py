import streamlit as st
import streamlit.components.v1 as components
from streamlit_local_storage import LocalStorage

from openai import OpenAI
ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

local_storage = LocalStorage()

if "todo_list" not in st.session_state:
    saved = local_storage.getItem("todo_list")

    if saved:
        st.session_state.todo_list = saved
    else:
        st.session_state.todo_list = []
if 'user_motto' not in st.session_state:
    st.session_state.user_motto = "오늘도 화이팅!"
if 'motto_updated' not in st.session_state:
    st.session_state.motto_updated = False
if 'clear_list' not in st.session_state:
    st.session_state.clear_list = []
def save_todo():
    local_storage.setItem(
        "todo_list",
        st.session_state.todo_list
    )
    local_storage.setItem(
        "clear_list",
        st.session_state.clear_list
    )
def add_todo():
    task = st.session_state.todo_input
    if task:
        st.session_state.todo_list.append([task, False])
        save_todo()
        st.toast("할 일이 추가되었습니다!")
        st.session_state.todo_input = ""      
def page_todo():
    st.header("오늘의 할 일")
    st.write(f"현재 다짐: **{st.session_state.user_motto}**")

    new_todo = st.text_input("추가할 할 일을 입력하세요", key="todo_input")

    st.button("추가하기", on_click=add_todo)

    if new_todo == "":
        st.warning("할 일을 입력하고 버튼을 눌러주세요!")

    st.markdown("---")

    for i in range(len(st.session_state.todo_list)):
        col_task, col_btn, col_status = st.columns([4, 1, 1])

        with col_task:
            st.write(f"{i+1}. {st.session_state.todo_list[i][0]}")

        with col_btn:
            if st.button("완료", key=f"complete_{i}"):
                st.session_state.clear_list.append(st.session_state.todo_list[i])
                st.session_state.todo_list.pop(i)


                # 완료 상태 저장
                save_todo()

                st.rerun()
            if st.button("제거", key=f"delete_{i}"):
                st.session_state.todo_list.pop(i)

                # 제거
                save_todo()

                st.rerun()

        with col_status:
            if st.session_state.todo_list[i][1]:
                st.write("✅ **달성!**")

    st.markdown("---")
def page_report():
    st.header("AI가 짜주는 세부 목표 ")
    if not st.session_state.todo_list:
        st.write("아직 등록된 할 일이 없습니다.")
    else:
        total = len(st.session_state.todo_list)
        count = 0
        for item in st.session_state.todo_list:
            if item[1] == True:
                count += 1
        progress = (count / total) * 100
        st.metric("오늘의 달성률", f"{progress:.1f}%")
        st.progress(progress / 100)
        if progress == 100:
            st.balloons()
            st.success("모든 목표를 달성하셨습니다! 🏆")
        if st.button("기록 전체 초기화"):
            st.session_state.todo_list = []
            st.rerun()

def page_ai_coach():
    st.header("🧐 AI 코치와 대화하기")
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "너는 사용자의 할 일 목록과 달성 정도를 분석하여 조언하는 열정적인 코치야. 사용자가 더 멋진 삶을 살 수 있도록 명확한 조언과 응원해줘."}
        ]
        
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
    question = st.chat_input("질문을 입력하세요")
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            status_context = f"현재 나의 할 일과 달성 여부: {st.session_state.todo_list}"
            prompt = st.session_state.messages + [{"role": "system", "content": status_context}]
            with st.spinner("AI 코치가 생각 중...🤔"):
                response = ai_client.chat.completions.create(
                    model="gpt-5.4-mini",
                    messages=prompt)
                ai_response = response.choices[0].message.content
                st.markdown(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

pg = st.navigation([
    st.Page(page_todo, title="오늘의 할 일"),
    st.Page(page_report, title="나의 갓생 지수", icon="📈"),
    st.Page(page_ai_coach, title="AI 코칭", icon="🧐")], position="top")

##st.title("🌱 갓생 살기 플래너")
pg.run()
