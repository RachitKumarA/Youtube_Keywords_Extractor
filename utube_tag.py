import streamlit as st
from bs4 import BeautifulSoup
import requests
st.markdown("<h1 style='text-align: center;'>Youtube Keywords Extractor</h1>", unsafe_allow_html=True)
st.markdown(" --- ", unsafe_allow_html=True)
url=st.text_input("Youtube URL Here")
if url:
    page=requests.get (url)
    soup=BeautifulSoup(page.content, 'lxml')
    meta_tag=soup.select("meta[name='keywords']")
    tit=soup.find("title")
    keywords=meta_tag[0]["content"]
    st.title("Title")
    st.markdown(f"<h4>{tit.text}</h4>", unsafe_allow_html=True)
    st. title("Tags")
    st.markdown(f"<h5>{keywords}</h5>", unsafe_allow_html=True)
