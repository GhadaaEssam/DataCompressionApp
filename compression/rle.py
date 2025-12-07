def rle_encode(text: str) -> str:
    if not text:
        return ""

    encoded = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{text[i-1]}")  # number first
            count = 1

    encoded.append(f"{count}{text[-1]}")
    return "".join(encoded)


def rle_decode(encoded: str) -> str:
    if not encoded:
        return ""

    decoded = []
    count = ""

    for c in encoded:
        if c.isdigit():
            count += c
        else:
            if count == "":
                raise ValueError(f"Missing count before character '{c}'")
            decoded.append(c * int(count))
            count = ""

    return "".join(decoded)