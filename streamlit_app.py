import streamlit as st



# Streamlit 라이브러리와 무작위 선택을 위한 random 라이브러리를 가져옵니다.
import streamlit as st
import random

# --- 앱 구조 설계 ---

# 1. 앱 제목 설정
# st.title() 함수를 사용하여 웹 앱의 제목을 "행운의 색깔"로 표시합니다.
st.title("🎨 행운의 색깔")
st.write("버튼을 눌러 오늘의 행운 색깔을 확인해보세요!")

# 2. 버튼 스타일링 (요구사항: 검은색 배경에 하얀색 글씨)
# st.button 위젯은 직접적인 색상 변경을 지원하지 않습니다.
# 따라서 st.markdown과 CSS를 사용하여 버튼 스타일을 적용합니다.
# 이 코드는 앱에 있는 첫 번째 버튼의 스타일을 변경합니다.
st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #000000; /* 검은색 배경 */
        color: #FFFFFF; /* 하얀색 글씨 */
        border: 1px solid #000000; /* 검은색 테두리 */
    }
    div.stButton > button:hover {
        background-color: #333333; /* 마우스를 올렸을 때 약간 밝은 회색 */
        color: #FFFFFF;
        border: 1px solid #000000;
    }
</style>""", unsafe_allow_html=True)


# 3. 데이터 준비
# 뽑기 대상이 될 색깔들의 리스트를 정의합니다.
color_list = [
    "❤️빨간색❤️", "🧡주황색🧡", "💛노랑색💛", "💚초록색💚", "🩵하늘색🩵",
    "💙파란색💙", "💜보라색💜", "💗핑크색💗", "🤍하얀색🤍", "🖤검은색🖤", "🤎갈색🤎","🩶회색🩶"
]

# 4. 세션 상태(Session State) 초기화
# 앱이 새로고침 되어도 선택된 색깔을 기억하기 위해 세션 상태를 사용합니다.
# 'lucky_color' 라는 키가 세션 상태에 없으면, 초기값으로 None (값 없음)을 설정합니다.
if 'lucky_color' not in st.session_state:
    st.session_state.lucky_color = None

# 5. 핵심 로직 구현 (버튼 클릭)
# '뽑기' 버튼을 생성하고, 사용자가 이 버튼을 클릭하면 True가 됩니다.
if st.button("오늘 나의 행운 색깔은?"):
    # color_list에서 무작위로 하나의 색깔을 선택합니다.
    picked_color = random.choice(color_list)
    # 선택된 색깔을 세션 상태의 'lucky_color'에 저장합니다.
    st.session_state.lucky_color = picked_color

# 6. 결과 출력
# 세션 상태에 저장된 행운의 색깔이 있으면 (None이 아니면) 화면에 표시합니다.
if st.session_state.lucky_color:
    # st.subheader()를 사용하여 조금 더 큰 폰트로 결과를 보여줍니다.
    st.subheader(f"당신의 행운 색깔은 **'{st.session_state.lucky_color}'** 입니다!")