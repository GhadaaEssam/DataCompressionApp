# image_helpers.py

import numpy as np
from PIL import Image

def load_image(file) -> np.ndarray:
    """Load image from file (uploaded via Streamlit)"""
    img = Image.open(file).convert("RGB")
    return np.array(img)

def save_image(array: np.ndarray, filepath: str):
    """Save numpy array as image file"""
    img = Image.fromarray(array.astype(np.uint8))
    img.save(filepath)

def resize_image(image_array: np.ndarray, width: int, height: int) -> np.ndarray:
    """Resize numpy image array to new dimensions"""
    img = Image.fromarray(image_array.astype(np.uint8))
    img = img.resize((width, height))
    return np.array(img)