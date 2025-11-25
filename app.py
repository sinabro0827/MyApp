import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout='wide')

st.title('hello, streamlit!')
df = pd.DataFrame({
    '이름': ['홍길동', '김철수'],
    '나이': [25, 30],
    'address':['서울','화성']
})

st.dataframe(df)         # 스크롤 가능한 표
st.table(df)             # 정적인 표

fig, ax = plt.subplots()
ax.plot([1,2,3],[10,20,30])
st.pyplot(fig)

name = st.text_input("이름을 입력하세요")
age = st.number_input("나이", min_value=0, max_value=120)
agree = st.checkbox("동의하십니까?")
choice = st.selectbox("메뉴 선택", ['김밥', '라면', '떡볶이'])
button = st.button("클릭!")

#사이드바 활용
st.sidebar.title("사이드 메뉴")
option = st.sidebar.selectbox("옵션 선택", ['옵션 1', '옵션 2'])
st.write('선택한 옵션:', option)
#파일 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

col1, col2, col3 = st.columns([2,1,1])
with col1:
  st.header("고양이")
  st.image("https://www.developerfastlane.com/img/blog/streamlit/cat.webp", use_container_width=True)
with col2:
  st.header("강아지")
  st.image("https://www.developerfastlane.com/img/blog/streamlit/dog.webp", use_container_width=True)
with col3:
  st.header("부엉이")
  st.image("https://www.developerfastlane.com/img/blog/streamlit/owl.webp", use_container_width=True)


tab1, tab2, tab3 = st.tabs(['탭 1', '탭 2', '탭 3'])

with tab1:
    st.header('탭 1 콘텐츠')
    st.write('이곳에 탭 1의 콘텐츠를 배치합니다.')

with tab2:
    st.header('탭 2 콘텐츠')
    st.write('이곳에 탭 2의 콘텐츠를 배치합니다.')

with tab3:
    st.header('탭 3 콘텐츠')
    st.write('이곳에 탭 3의 콘텐츠를 배치합니다.')

#상태표시
st.success("성공 메시지")
st.warning("경고 메시지")
st.error("에러 메시지")
st.info("정보 메시지")


st.markdown(
    """
    <style>
    .left-align {
        text-align: left;
    }
    .right-align {
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<p class="left-align">이 텍스트는 왼쪽으로 정렬되어 있습니다.</p>', unsafe_allow_html=True)
st.markdown('<p class="right-align">이 텍스트는 오른쪽으로 정렬되어 있습니다.</p>', unsafe_allow_html=True)


with st.container():
    st.header('컨테이너 내의 내용')
    st.write('여기에는 다양한 UI 컴포넌트를 추가할 수 있습니다.')