import streamlit as st
from compression.quantization import apply_quantization
from utils.image_helpers import load_image, save_image
from utils.metrics import calculate_mse, calculate_psnr
from PIL import Image
import numpy as np

st.title("Lossy Image Compression (Quantization)")

uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
level = st.slider("Quantization Level", 1, 100, 50)

if uploaded_image is not None:
    original_image = load_image(uploaded_image)

    # Display original and compressed side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(original_image, caption="Original Image", width=300)

    if st.button("Apply Quantization"):
        compressed_image = apply_quantization(original_image, level)

        with col2:
            st.image(compressed_image, caption="Compressed Image", width=300)

        # Metrics
        mse = calculate_mse(original_image, compressed_image)
        psnr = calculate_psnr(original_image, compressed_image)
        st.write(f"**MSE:** {mse:.2f}")
        st.write(f"**PSNR:** {psnr:.2f} dB")

        # Save and download compressed image
        save_image(compressed_image, "compressed_image.png")
        with open("compressed_image.png", "rb") as f:
            st.download_button(
                "Download Compressed Image",
                f,
                file_name="compressed_image.png",
                mime="image/png"
            )