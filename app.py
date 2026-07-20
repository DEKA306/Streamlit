import streamlit as st

st.markdown("# 앱 UI 만들기")
user_id = st.text_input("이름", placeholder="example_user")

ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
tone = st.selectbox("답변의 말투를 골라주세요", ["친절하게", "냉철하게", "유머러스하게"])
features = st.multiselect("추가 기능을 선택하세요", ["이미지 생성", "웹 검색", "코드 분석", "번역"])
creativity = st.slider("AI의 창의성 수준을 설정하세요", 0, 100, 50)
ai_speed = st.select_slider("응답 처리 속도를 선택하세요",options=["매우 느림", "느림", "보통", "빠름", "실시간"],value="보통")
agree = st.checkbox("개인정보 수집 및 AI 학습 이용에 동의합니다.")
st.markdown("---")

if st.button("질문 전송하기"):
    if agree:
        st.success(f"성공적으로 전송되었습니다! ({user_id}님)")
        st.markdown(f"""
        * **질문 내용:** {question}
        * **선택 모델:** `{ai_model}` | **말투:** `{tone}`
        * **활성화 기능:** {', '.join(features) if features else '없음'}
        * **창의성:** `{creativity}%` | **처리 속도:** `{ai_speed}`
        """)
        
        if age < 14:
            st.info("참고: 14세 미만 사용자이므로 보호자 모드가 활성화됩니다.")
    else:
        st.error("⚠️ 동의 항목에 체크해야 전송이 가능합니다.")
