import streamlit as st

# 기본 설정
st.set_page_config(#브라우저 상단에 타이틀 생성
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",#화면을 채움
)


# # 세로로 나누기
col1, col2, col3 = st.columns(3)#세로로 3등분

with col1:
   #col1,2,3를 지정
   st.header("HAPPY")
   st.image("exe1.jpg")

with col2:
    
    st.header("NEW YEAR")
    st.image("exe2.png")

with col3:    
    st.header("구리로봇&SW코딩영재원")
    st.image("exe3.png")


st.video("https://www.youtube.com/watch?v=gQdxBOb8OyI&pp=ygUTMjAyNeyLoOuFhOuPmeyYgeyDgQ%3D%3D")


# 사이드바
with st.sidebar:#사이드바 생성
    add_radio = st.radio(
        "방문을 환영합니다",
        ("TEL:070-4115-8222", "구리로봇학원")
    )

