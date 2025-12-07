import streamlit as st

st.set_page_config(page_title="Data Compression App", layout="wide", page_icon="📦")
st.image("assets/home.png",width=200)

st.title("Data Compression Application")

st.write("""
Welcome to the Data Compression App!  

- Use the sidebar to navigate to **Lossless Compression** or **Lossy Compression**.
- Lossless supports RLE, Huffman, LZW, and Golomb for text/binary files.
- Lossy supports image compression using Quantization.

**Team Members:**
1. Toka Mohamed
2. Alaa Sayed
3. Ghada Essam
""")
