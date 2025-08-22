import streamlit as st



# 필요한 라이브러리를 불러옵니다.
import streamlit as st
import random

# --- 앱 구조 설계 ---

# 1. 앱 제목 설정
st.title("🍀 행운의 색깔과 명언 뽑기")
st.write("버튼을 눌러 오늘의 행운을 확인해보세요!")

# 2. 데이터 준비
# 색상, 운세 점수, 명언에 대한 데이터를 미리 정의합니다.
# 각 색상에 대한 정보(이름, 이모지, CSS 색상 코드)를 딕셔너리 리스트로 관리하여 확장성을 높입니다.
colors = [
    {"name": "빨간색", "emoji": "❤️", "code": "#FF4B4B"},
    {"name": "주황색", "emoji": "🧡", "code": "#FF8C00"},
    {"name": "노랑색", "emoji": "💛", "code": "#FFD700"},
    {"name": "초록색", "emoji": "💚", "code": "#2E8B57"},
    {"name": "하늘색", "emoji": "🩵", "code": "#87CEEB"},
    {"name": "파란색", "emoji": "💙", "code": "#4682B4"},
    {"name": "보라색", "emoji": "💜", "code": "#9370DB"},
    {"name": "핑크색", "emoji": "🩷", "code": "#FFC0CB"},
    {"name": "하얀색", "emoji": "🤍", "code": "#F0F2F6"}, # 밝은 회색으로 표현
    {"name": "검은색", "emoji": "🖤", "code": "#0E1117"},
    {"name": "갈색", "emoji": "🤎", "code": "#A0522D"},
    {"name": "회색", "emoji": "🩶", "code": "#808080"}
]

quotes = [
    "시간은 금입니다.", "아는 것이 힘입니다.", "피할 수 없으면 즐기세요.",
    "행동이 말보다 큽니다.", "웃음은 최고의 약입니다.", "시작이 반입니다.",
    "포기하지 마세요.", "고통 없인 얻는 것도 없습니다.", "진실은 반드시 이깁니다.",
    "행복은 선택입니다.", "내일은 또 다른 기회입니다.", "단순함이 최고의 정교함입니다.",
    "실패는 성공의 어머니입니다.", "꿈꾸는 자만이 이룹니다.", "작은 변화가 큰 차이를 만듭니다.",
    "용기는 두려움의 반대가 아닙니다.", "스스로를 이기세요.", "오늘을 사세요.", "끝까지 가세요."
]


# 3. 세션 상태(Session State) 초기화
# 앱이 재실행되어도 이전 결과가 유지되도록 세션 상태를 사용합니다.
# 'result' 키가 없으면 초기값으로 None을 설정합니다.
if 'result' not in st.session_state:
    st.session_state.result = None

# 4. 핵심 로직 함수 정의
# 뽑기 버튼을 누를 때마다 실행될 함수를 만듭니다.
def draw_lucky_item():
    """행운의 색깔, 점수, 명언을 무작위로 선택하여 세션 상태에 저장합니다."""
    lucky_color = random.choice(colors)
    lucky_score = random.randint(70, 100)
    lucky_quote = random.choice(quotes)

    # 뽑은 결과를 딕셔너리 형태로 묶어서 세션 상태에 저장합니다.
    st.session_state.result = {
        "color": lucky_color,
        "score": lucky_score,
        "quote": lucky_quote
    }

# 5. UI 요소 배치 (버튼)
# st.columns를 사용하여 버튼 두 개를 나란히 배치합니다.
col1, col2 = st.columns(2)

with col1:
    # '뽑기' 버튼을 만들고, 클릭 시 draw_lucky_item 함수를 실행합니다.
    st.button("행운 뽑기!", on_click=draw_lucky_item, key="draw_button", use_container_width=True)

with col2:
    # '다시 뽑기' 버튼도 동일한 기능을 수행하도록 설정합니다.
    st.button("다시 뽑기!", on_click=draw_lucky_item, key="redraw_button", use_container_width=True)

# 6. 결과 출력
# 세션 상태에 결과가 저장되어 있는 경우에만 결과를 화면에 표시합니다.
if st.session_state.result:
    st.write("---") # 구분을 위한 가로선

    # 저장된 결과들을 변수로 받아옵니다.
    result_color = st.session_state.result["color"]
    result_score = st.session_state.result["score"]
    result_quote = st.session_state.result["quote"]

    # 보기 좋게 정렬된 결과 메시지를 생성합니다.
    st.subheader(f"오늘의 행운 색깔은? {result_color['emoji']} {result_color['name']}")
    st.subheader(f"오늘의 운세 점수는? 🎰 {result_score}점")

    # 명언의 글자색을 행운의 색깔과 맞추기 위해 HTML/CSS를 사용합니다.
    # unsafe_allow_html=True를 설정해야 HTML 태그가 적용됩니다.
    st.markdown(
        f"""
        <p style='
            color:{result_color['code']};
            font-size:1.3em;
            font-weight:bold;
            text-align:center;
            border: 2px solid {result_color['code']};
            border-radius: 10px;
            padding: 10px;
        '>
            "{result_quote}"
        </p>
        """,
        unsafe_allow_html=True
    )


# 7. 버튼 스타일링 (CSS)
# 모든 버튼에 검은색 배경과 하얀색 글씨를 적용하는 CSS 코드입니다.
# st.markdown을 사용하여 앱 전체에 스타일을 적용합니다.
st.markdown("""
<style>
    div.stButton > button {
        background-color: #000000; /* 검은색 배경 */
        color: #FFFFFF; /* 하얀색 글씨 */
        border: 1px solid #000000;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #333333; /* 마우스를 올렸을 때 약간 밝은 회색 */
        color: #FFFFFF;
        border: 1px solid #333333;
    }
</style>""", unsafe_allow_html=True)