import streamlit as st
import time


st.set_page_config(page_title="Animation", layout="wide")


st.markdown("""
<style>
@keyframes move {
  0%   {transform: translateX(0px);}
  50%  {transform: translateX(300px);}
  100% {transform: translateX(0px);}
}

.moving-text {
  font-size: 48px;
  font-weight: bold;
  color: #ff4b4b;
  animation: move 5s infinite;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<p class="moving-text"> Streamlit Animation Demo </p>', unsafe_allow_html=True)


st.write("Animation Demo")

st.success("correct")
