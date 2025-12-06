def rle_encode(data: bytes) -> bytes:
    out = []
    if not data: return b""
    c, n = data[0], 1
    for b in data[1:]:
        if b == c and n < 255: n += 1
        else: out += [n, c]; c, n = b, 1
    out += [n, c]
    return bytes(out)

def rle_decode(data: bytes) -> bytes:
    out = []
    it = iter(data)
    for n in it:
        v = next(it)
        out += [v]*n
    return bytes(out)
