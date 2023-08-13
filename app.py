import streamlit as st
import requests
from bs4 import BeautifulSoup

def extract_headers(url):
    headers_list = []
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            headers_list.append(f"{header.name}: {header.text.strip()}")
    except Exception as e:
        st.write(f"An error occurred: {e}")
    return headers_list

st.title('Website Header Extractor')

url = st.text_input('Enter a URL:', '')
if url:
    headers = extract_headers(url)
    for header in headers:
        st.write(header)
