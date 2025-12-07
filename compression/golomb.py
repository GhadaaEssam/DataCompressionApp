import math
from collections import Counter

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

# --- Decoding Function ---
def golomb_decode(bitstream, m):
    # decode unary
    q = 0
    i = 0
    while i < len(bitstream) and bitstream[i] == "1":
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
        consumed = i + (b - 1)  # Changed: total consumed from start
    else:
        r_bits = bitstream[i:i+b]
        val = int(r_bits, 2)
        r = val - threshold
        consumed = i + b  # Changed: total consumed from start
    
    x = q * m + r
    return x, consumed