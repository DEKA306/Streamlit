import streamlit as st
import streamlit.components.v1 as components
from streamlit_local_storage import LocalStorage
import json
from openai import OpenAI

ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

local_storage = LocalStorage()

st.title("AI Task Manager")

def pg1():
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
    
            data = {
                "main_goal": task,
                "tasks": tasks
            }
    
            local_storage.setItem("app_data", data)
    
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
def pg2():
    st.title("AI가 짜주는 세부 목표")

    data = local_storage.getItem("app_data")

    if data:
        main_goal = data["main_goal"]
    else:
        main_goal = None

    if main_goal:
        st.write("현재 목표:")
        st.info(main_goal)

        if st.button("세부 목표 만들기"):
        
            response = ai_client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": """
        너는 목표 관리 AI다.
        
        사용자의 큰 목표를 실행 가능한 세부 목표로 나눠라.
        
        반드시 아래 JSON 형식으로만 응답한다.
        
        {
          "main_goal": "큰 목표",
          "steps": [
            {
              "title": "세부 목표 제목",
              "description": "해야 할 일 설명",
              "duration": "예상 기간",
              "priority": "우선순위"
            }
          ]
        }
        
        steps는 3~7개를 만든다.
        설명은 실제 행동 가능한 내용으로 작성한다.
        """
        },
        {
            "role": "user",
            "content": main_goal
        }
    ]
)

            result = response.choices[0].message.content

            # --- [출력 부분 수정] ---
            try:
                result_data = json.loads(result)
                
                st.subheader(f"🎯 [{result_data.get('main_goal', main_goal)}] 실행 계획")
                st.markdown("---")

                steps = result_data.get("steps", [])
                
                for idx, step in enumerate(steps, 1):
                    with st.container(border=True):
                        col1, col2, col3 = st.columns([3, 1, 1])
                        
                        with col1:
                            st.markdown(f"### **Step {idx}. {step.get('title', '')}**")
                        with col2:
                            st.markdown(f"⏱️ **기간:** {step.get('duration', '-')}")
                        with col3:
                            st.markdown(f"🔥 **우선순위:** {step.get('priority', '-')}")
                        
                        st.write(step.get("description", ""))

            except json.JSONDecodeError:
                st.error("JSON 파싱 중 오류가 발생했습니다.")
                st.text(result)
            # ------------------------

    else:
        st.warning("먼저 1페이지에서 목표를 입력해주세요.")
pg = st.navigation(
    [
        st.Page(pg1, title="앞으로 해야할 큰 목표"),
        st.Page(pg2, title="AI가 짜주는 세부 목표")
    ],
    position="top"
)

pg.run()
