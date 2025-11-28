import numpy as np
from PIL import Image

def load_image(file):
    return np.array(Image.open(file).convert("RGB"))

def apply_quantization(img, level):
    return img

def calculate_mse(orig, comp):
    return float(np.mean((orig - comp) ** 2))

def calculate_psnr(orig, comp):
    mse = calculate_mse(orig, comp)
    if mse == 0:
        return float("inf")
    return 20 * np.log10(255.0 / np.sqrt(mse))
