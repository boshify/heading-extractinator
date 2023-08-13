import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title('Heading Extractinator')

@st.cache
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

urls = st.text_area("Enter up to 6 URLs (separated by new lines):").split("\n")

if urls:
    all_headings = []
    for url in urls:
        if url:  # Check if the string is not empty
            headings = extract_headings(url)
            all_headings.extend(headings)
            st.write(f"\nURL {url}\n")
            for heading in headings:
                st.markdown(heading, unsafe_allow_html=True)

    # Join all headings and create a copy button
    combined_headings = "\n".join(all_headings)
    copy_html = """
        <textarea id="copyText" style="width:100%;height:100px;">{}</textarea>
        <button onclick="copyToClipboard()">Copy to Clipboard</button>
        <script>
            function copyToClipboard() {{
                var copyText = document.getElementById("copyText");
                copyText.select();
                document.execCommand("copy");
            }}
        </script>
    """.format(combined_headings)
    st.markdown(copy_html, unsafe_allow_html=True)
