import math
from collections import Counter

# --- Encoding Function ---
def golomb_encode(n, m):
    q = n // m
    r = n % m
    
    # unary for quotient
    unary = "1" * q + "0"
    
    # truncated binary for remainder
    b = (m - 1).bit_length()
    threshold = (1 << b) - m
    
    if r < threshold:
        remainder = f"{r:0{b-1}b}"
    else:
        r += threshold
        remainder = f"{r:0{b}b}"
    
    return unary + remainder

# --- 1. Calculate Entropy ---
def calculate_entropy(data):
    """
    Calculates Entropy of the dataset.
    Returns bits per symbol.
    """
    total_count = len(data)
    if total_count == 0: return 0.0
    
    counts = Counter(data)
    entropy = 0.0
    
    for count in counts.values():
        probability = count / total_count
        entropy += -probability * math.log2(probability)
        
    return entropy

# --- 3. Calculate Efficiency ---
def calculate_efficiency(entropy, avg_length):
    """
    Calculates the coding efficiency as a percentage.
    Formula: (Entropy / Average_Length) * 100
    """
    if avg_length == 0: return 0.0
    return (entropy / avg_length) * 100

# --- 4. Calculate Compression Ratio ---
def calculate_compression_ratio(data, m, original_bits_per_symbol=8):
    """
    Calculates the compression ratio.
    Formula: Number of Bits Before / Number of Bits After
    """
    total_count = len(data)
    if total_count == 0: return 0.0
    
    # Calculate sizes
    number_of_bits_before = total_count * original_bits_per_symbol
    
    number_of_bits_after = 0
    for n in data:
        code = golomb_encode(n, m)
        number_of_bits_after += len(code)
    
    if number_of_bits_after == 0: return 0.0
    
    return number_of_bits_before / number_of_bits_after

# --- Decoding Function ---
def golomb_decode(bitstream, m):
    # decode unary
    q = 0
    i = 0
    while bitstream[i] == "1":
        q += 1
        i += 1
    i += 1  # skip the '0'
    
    # truncated binary decode
    b = (m - 1).bit_length()
    threshold = (1 << b) - m
    
    r_bits = bitstream[i:i+b-1]
    val = int(r_bits, 2)
    
    if val < threshold:
        r = val
        consumed = b - 1
    else:
        r_bits = bitstream[i:i+b]
        val = int(r_bits, 2)
        r = val - threshold
        consumed = b
    
    x = q * m + r
    return x, i + consumed
