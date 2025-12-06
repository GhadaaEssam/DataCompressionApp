def read_file(filepath: str) -> bytes:
    with open(filepath, "rb") as f:
        return f.read()

def write_file(filepath: str, data: bytes):
    with open(filepath, "wb") as f:
        f.write(data)

def bytes_to_str(data: bytes) -> str:
    return data.decode()

def str_to_bytes(data: str) -> bytes:
    return data.encode()