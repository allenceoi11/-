import streamlit as st

st.set_page_config(page_title="My Streamlit App", layout="wide")

st.title("🎉 欢迎使用 Streamlit!")

st.write("""
这是一个部署在 Streamlit Community Cloud 上的应用。
""")

# 示例：计数器
st.header("交互式示例")

if "counter" not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ 增加"):
        st.session_state.counter += 1

with col2:
    st.metric("计数器", st.session_state.counter)

with col3:
    if st.button("➖ 减少"):
        st.session_state.counter -= 1

# 输入表单
st.header("表单输入")

with st.form("my_form"):
    name = st.text_input("输入您的名字:")
    submitted = st.form_submit_button("提交")
    
    if submitted:
        st.success(f"👋 你好, {name}!")

st.sidebar.success("设置选项完成！")
