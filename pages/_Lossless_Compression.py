import streamlit as st
from compression.rle import rle_encode, rle_decode 
from compression.huffman import huffman_encode, huffman_decode 
from compression.lzw import lzw_compress, lzw_decompress 
from compression.golomb import golomb_encode, golomb_decode 
from utils.metrics import compression_ratio

st.title("Lossless Compression")

# Initialize session state
if 'compressed_data' not in st.session_state:
    st.session_state.compressed_data = None
if 'huffman_tree' not in st.session_state:
    st.session_state.huffman_tree = None
if 'original_text' not in st.session_state:
    st.session_state.original_text = None

algorithm = st.selectbox("Select Algorithm", ["RLE", "Huffman", "LZW", "Golomb"])
uploaded_file = st.file_uploader("Upload text file", type=["txt"])

if uploaded_file is not None:
    # Read uploaded text
    text = uploaded_file.read().decode("utf-8")
    st.session_state.original_text = text
    
    st.write(f"Algorithm: {algorithm}")
    st.write(f"File: {uploaded_file.name}")
    
    col1, col2 = st.columns(2)
    
    # ------------------ COMPRESS ------------------
    with col1:
        if st.button("Compress"):
            if algorithm == "RLE":
                compressed = rle_encode(text)
                st.session_state.compressed_data = compressed
                st.session_state.huffman_tree = None
                
            elif algorithm == "Huffman":
                compressed, tree = huffman_encode(text)
                st.session_state.compressed_data = compressed
                st.session_state.huffman_tree = tree
                
            elif algorithm == "LZW":
                compressed = lzw_compress(text)
                st.session_state.compressed_data = compressed
                compressed = str(compressed)  # For display
                
            elif algorithm == "Golomb":
                m = 5
                # Convert text to list of ASCII values (integers)
                numbers = [ord(char) for char in text]
                # Encode each number and concatenate bitstreams
                compressed = ''.join([golomb_encode(num, m) for num in numbers])
                st.session_state.compressed_data = compressed
                st.session_state.huffman_tree = None
            
            ratio = compression_ratio(len(text), len(str(compressed)))
            st.success(f"Compression complete! Ratio: {ratio:.2f}")
            
            # Display compressed text
            st.subheader("Compressed Text")
            st.text_area("Output", str(compressed), height=200, key="comp_output")
            
            st.download_button(
                "Download Compressed File",
                data=str(compressed),
                file_name=f"compressed_{uploaded_file.name}",
                mime="text/plain"
            )
    
    # ------------------ DECOMPRESS ------------------
    with col2:
        if st.button("Decompress"):
            if st.session_state.compressed_data is None:
                st.error("Please compress the file first!")
            else:
                try:
                    if algorithm == "RLE":
                        decompressed = rle_decode(st.session_state.compressed_data)
                        
                    elif algorithm == "Huffman":
                        if st.session_state.huffman_tree is None:
                            st.error("Huffman tree not available. Compress first!")
                            decompressed = None
                        else:
                            decompressed = huffman_decode(
                                st.session_state.compressed_data, 
                                st.session_state.huffman_tree
                            )
                            
                    elif algorithm == "LZW":
                        decompressed = lzw_decompress(st.session_state.compressed_data)
                        
                    elif algorithm == "Golomb":
                        m = 5
                        bitstream = st.session_state.compressed_data
                        decoded_numbers = []
                        pos = 0
                        
                        # Decode each number from the bitstream
                        while pos < len(bitstream):
                            try:
                                num, consumed = golomb_decode(bitstream[pos:], m)
                                decoded_numbers.append(num)
                                pos += consumed
                            except:
                                break
                        
                        # Convert ASCII values back to text
                        decompressed = ''.join([chr(num) for num in decoded_numbers])
                    
                    if decompressed is not None:
                        st.success("Decompression complete!")
                        
                        # Display decompressed text
                        st.subheader("Decompressed Text")
                        st.text_area("Output", decompressed, height=200, key="decomp_output")
                        
                        # Verify if decompression matches original
                        if decompressed == st.session_state.original_text:
                            st.info("✓ Decompressed text matches original!")
                        else:
                            st.warning("⚠ Decompressed text differs from original")
                        
                        st.download_button(
                            "Download Decompressed File",
                            data=decompressed,
                            file_name=f"decompressed_{uploaded_file.name}",
                            mime="text/plain"
                        )
                        
                except Exception as e:
                    st.error(f"Decompression failed: {str(e)}")