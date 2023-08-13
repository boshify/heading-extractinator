import streamlit as st
import requests
from bs4 import BeautifulSoup

def extract_headings(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headings = []
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        indent = '    ' * (int(tag.name[1]) - 1)
        headings.append(f"{indent}<{tag.name}>{tag.text.strip()}</{tag.name}>")
    
    return headings

st.title('Website Header Extractor')

urls = []
for i in range(1, 7):
    url = st.text_input(f"Enter URL {i}:", "")
    if url:
        urls.append(url)

if st.button("Extract Headers"):
    for url in urls:
        st.write(f"URL: {url}")
        headings = extract_headings(url)
        for heading in headings:
            st.markdown(heading, unsafe_allow_html=True)
