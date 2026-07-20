import streamlit as st

st.markdown("# 앱 UI 만들기")
user_id = st.text_input("이름", placeholder="example_user")

ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)

age = st.number_input("반", min_value=1, max_value=11, value=3)


ai_speed = st.select_slider("난이도",options=["쉬움", "보통", "빠름"],value="보통")
creativity = st.slider("점수", 0, 50, 100)

question = st.text_area("소감", placeholder="소감입니다.")

if st.button("확인"):
    st.success(user_id+"/"+str(ai_model)+"학년/"+str(age)+"반/"+ai_speed)
    st.info("소감 : " + question)
    st.markdown(f"""
        * **점수:** `{creativity}%`
        """)
