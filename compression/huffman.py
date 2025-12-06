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
    file_size = len(data)
    if file_size == 0:
        return {}

    freq = Counter(data)

    # Normalize frequencies to probabilities
    for char in freq:
        freq[char] /= file_size

    freq_sorted = sorted(freq.items(), key=lambda item: item[1])
    freq = {item[0]: round(item[1], 4) for item in freq_sorted}

    nodes = [(p, ch) for ch, p in freq.items()]
    return nodes


def build_huffman_tree(nodes):
    heap = []

    # Convert frequency table to HuffmanNodes
    for freq, ch in nodes:
        heapq.heappush(heap, HuffmanNode(ch, freq))

    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    root = heap[0]
    return root


def build_codes(root):
    codes = {}

    def traverse(node, code):
        if node is None:
            return

        # Leaf node (actual character)
        if node.char is not None:
            codes[node.char] = code
            return

        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")
    return codes


def huffman_encode(data: str):
    if not data:
        return "", None

    nodes = build_frequency_table(data)
    root = build_huffman_tree(nodes)
    codes = build_codes(root)

    encoded = ""
    for ch in data:
        encoded += codes[ch]

    return encoded, root


def huffman_decode(bitstring: str, tree):
    decoded = ""
    current = tree

    for bit in bitstring:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        # If we reach a leaf node
        if current.char is not None:
            decoded += current.char
            current = tree

    return decoded


