import streamlit as st

def reset_all():
    st.session_state.user_name = ''
    st.session_state.weather = '맑음'
    st.session_state.top_type = '후드티'
    st.session_state.top_color = '밝음'
    st.session_state.bottom_type = '청바지'
    st.session_state.bottom_color = '슬림'
    st.session_state.shoes = '스니커즈'
    st.session_state.acc = []

with st.sidebar:
    st.header("프로필")
    user_name = st.text_input("닉네임", key="user_name")
    weather = st.selectbox("오늘 날씨", ["맑음", "흐림", "비/눈", "매우 추움"])
    st.markdown("---")
    st.info(f"반가워요, {user_name}님! 오늘 날씨는 `{weather}`이네요.")

st.title("👗 AI 코디 메이커")
st.write("사이드바에서 날씨를 먼저 선택하고 코디를 시작하세요!")
st.header("아이템 조합하기")
col1, col2 = st.columns(2)
with col1:
    st.subheader("상의")
    top_type = st.radio("종류", ["후드티", "셔츠", "맨투맨", "반팔 티셔츠"])
    top_color = st.select_slider("색상 톤", options=["밝음", "무난함", "어두움"])
with col2:
    st.subheader("하의")
    bottom_type = st.radio("종류", ["청바지", "슬랙스", "트레이닝 팬츠", "반바지"])
    bottom_color = st.select_slider("핏(Fit)", options=["슬림", "레귤러", "오버핏"])

st.header("디테일 추가")
tab1, tab2 = st.tabs(["신발", "악세서리"])
with tab1:
    st.write("오늘의 발걸음을 책임질 신발:")
    shoes = st.selectbox("신발 선택", ["스니커즈", "운동화", "구두", "슬리퍼"])
    with st.expander("신발 선택 팁 보기"):
        st.info("너무 튀는 신발은 지양하도록해요!")
with tab2:
    st.write("포인트 아이템:")
    acc = st.multiselect("악세서리 추가", ["모자", "안경", "목걸이", "가방"])
    with st.expander("악세서리 스타일링 팁 보기"):
        st.warning("너무 튀는 신발은 지양하도록해요!")
st.markdown("---")
if st.button("코디 완성하기"):
    with st.container(border=True):
        st.subheader(f"{user_name}님의 오늘의 룩북")
        st.write(f"오늘같은 **{weather}** 날씨에는 이렇게 입어보세요!")
        st.markdown(f"""
        * **상의:** {top_color} {top_type}
        * **하의:** {bottom_color} {bottom_type}
        * **매칭:** {shoes}와 {', '.join(acc) if acc else '악세서리 없이 깔끔하게!'}
        """)
        st.success("오늘의 스타일링이 완성되었습니다! 자신 있게 외출하세요! ")
        with st.expander("리사 수의 얼굴 보기"):
            st.image("https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRsTC_syMjfJll8-97bgSnlrm6-VYamikTdD7OTuIz4QAvifIECuxYXn3L4p5jHK8wL6FHLUtuECdWIUyK4LlYl_CGPSjx_vvN3EqUewx0_9CxyH7LNNX89me_Mx-gN8SPpdSlDpAS2rss&s=19")
            st.write("킹갓제너럴엠퍼러 AMD의 1황 리사수")
        with st.expander("젠슨 황의 얼굴보기"):
            st.image("https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcR6AMajS0WEb2ufnoV8dkTkQntbkJtFI6J5PCm3ntfdRlBGW_nqpuZykqyUGu-A35t46efFodQzhYeDDmA4xulNgNEPFKQomEzl3w94yskW5COA_-OZgvRqpXW1sIYHyhOHc892rUfc7OAD&s=19")
            st.write("최고의 그래픽카드")
st.button('전체 초기화', on_click=reset_all)
