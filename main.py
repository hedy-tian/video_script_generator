import streamlit as st
from utils import generate_script

st.title("🎬视频脚本生成器")
st.divider()

with st.sidebar:
    api_key = st.text_input("请输入Gemini API密钥：", type="password")
    st.markdown("[获取Gemini API密钥](https://aistudio.google.com/app/apikey) ")

subject = st.text_input("🌟请输入视频的主题")
st.divider()
video_length = st.number_input("⏰请输入视频的大致时长（单位：分钟）",min_value=0.1,max_value=5.0,step=0.1)
st.divider()
creativity = st.slider("💡请输入视频脚本的创造力（数值越小代表更严谨，数值越大代表更多样)",
          min_value=0.1,max_value=1.0,step=0.1,value=0.2)
st.divider()
submit = st.button("生成脚本")

if submit and not api_key:
    st.info("请输入你的Gemini API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频时长必须大于或等于0.1")
    st.stop()

if submit:
    with st.spinner("AI正在思考，请耐心等待..."):
        script, title, search_result = generate_script(subject,video_length,creativity,api_key)
    st.success("视频脚本已生成！")
    st.subheader("📝 标题:")
    st.markdown(title)
    st.subheader("🎭 脚本：")
    st.markdown(script)
    with st.expander("🔍 展开维基百科相关搜索"):
        st.info(search_result)

