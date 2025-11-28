import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(data: str):
    return Counter(data)

def build_huffman_tree(freq_table):
    pass

def build_codes(root):
    return {}

def huffman_encode(data: str):
    return "", None

def huffman_decode(bitstring: str, tree):
    return ""
