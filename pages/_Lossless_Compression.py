import streamlit as st
from compression.rle import rle_encode, rle_decode
from compression.huffman import huffman_encode, huffman_decode
from compression.lzw import lzw_compress, lzw_decompress
from compression.golomb import golomb_encode, golomb_decode
from utils.io_utils import bytes_to_str, str_to_bytes
from utils.metrics import compression_ratio

st.title("Lossless Compression")

algorithm = st.selectbox("Select Algorithm", ["RLE", "Huffman", "LZW", "Golomb"])
uploaded_file = st.file_uploader("Upload text/binary file", type=["txt", "bin"])

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    st.write(f"Algorithm: {algorithm}")
    st.write(f"File: {uploaded_file.name}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Compress"):
            if algorithm == "RLE":
                compressed = rle_encode(file_bytes)
            elif algorithm == "Huffman":
                compressed, tree = huffman_encode(bytes_to_str(file_bytes))
                compressed = str_to_bytes(compressed)
            elif algorithm == "LZW":
                compressed = lzw_compress(bytes_to_str(file_bytes))
                compressed = str_to_bytes(str(compressed))
            elif algorithm == "Golomb":
                m = 5
                compressed = golomb_encode(list(file_bytes), m).encode()

            ratio = compression_ratio(len(file_bytes), len(compressed))
            st.success(f"Compression complete! Ratio: {ratio:.2f}")
            st.download_button(
                "Download Compressed File",
                data=compressed,
                file_name=f"compressed_{uploaded_file.name}"
            )

    with col2:
        if st.button("Decompress"):
            if algorithm == "RLE":
                decompressed = rle_decode(file_bytes)
            elif algorithm == "Huffman":
                decompressed = huffman_decode(bytes_to_str(file_bytes), None).encode()
            elif algorithm == "LZW":
                decompressed = lzw_decompress(eval(bytes_to_str(file_bytes))).encode()
            elif algorithm == "Golomb":
                m = 5
                decompressed = bytes(golomb_decode(bytes_to_str(file_bytes), m))

            st.success("Decompression complete!")
            st.download_button(
                "Download Decompressed File",
                data=decompressed,
                file_name=f"decompressed_{uploaded_file.name}"
            )
