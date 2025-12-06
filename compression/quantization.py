import numpy as np
from PIL import Image

def load_image(file):
    return np.array(Image.open(file).convert("RGB"))

def apply_quantization(img, level):
    """
    Uniform quantization
    Args:
        img: numpy array of the image (H x W x 3)
        level: quantization level (number of bits per channel)
               Higher level = more quality, less compression
               Lower level = less quality, more compression
    
    Returns:
        quantized image as numpy array
    """
    # Step size
    step = 256 // level

    # Quantize the image:
    # 1. Divide pixel values by step size to get bin indices
    # 2. Round to get integer bin indices
    # 3. Multiply back by step size to get quantized values
    quantized = (img // step) * step

    # Clip values to valid range [0, 255]
    return np.clip(quantized, 0, 255).astype(np.uint8)

def decode_quantization(q_img, level):
    step = 256 // level
    reconstructed = q_img + step // 2
    return np.clip(reconstructed, 0, 255).astype(np.uint8)

def calculate_mse(orig, comp):
    return float(np.mean((orig - comp) ** 2))

def calculate_psnr(orig, comp):
    mse = calculate_mse(orig, comp)
    if mse == 0:
        return float("inf")
    return 20 * np.log10(255.0 / np.sqrt(mse))
