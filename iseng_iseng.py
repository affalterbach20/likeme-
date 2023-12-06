import streamlit as st
from PIL import Image
import time

st.title("You like me?")
gambar = st.image("emoji.jpg",width=300)
col1,col2 = st.columns([1,2],gap="small")
with col1:
    yes = st.button("Yes....")
with col2:
    no = st.button("No.....")
if yes:
    with st.spinner("tunggu!!"):
        time.sleep(3)
    st.title("I Love You......")
    st.image("OIP.jpeg",width=300)
    st.balloons()
if no:
    with st.spinner("tunggu!!"):
        time.sleep(3)
    st.title("Fuck You!!.....")
    st.image("fuck.jpg",width=300)