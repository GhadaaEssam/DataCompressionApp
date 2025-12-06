import numpy as np

def compression_ratio(original_size: int, compressed_size: int) -> float:
    if compressed_size == 0:
        return 0
    return original_size / compressed_size

def calculate_mse(original: np.ndarray, compressed: np.ndarray) -> float:
    return float(np.mean((original - compressed) ** 2))

def calculate_psnr(original: np.ndarray, compressed: np.ndarray) -> float:
    mse = calculate_mse(original, compressed)
    if mse == 0:
        return float("inf")
    max_pixel = 255.0
    return 20 * np.log10(max_pixel / np.sqrt(mse))