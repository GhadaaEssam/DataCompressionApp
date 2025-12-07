import binascii

def lzw_compress(data: str):
    dictionary = {chr(i): i for i in range(256)}
    next= 256
    word = ""
    output = []
    for char in data:
        next_comp = word + char
        if next_comp in dictionary:
            word = next_comp
        else:
            output.append(dictionary[word])
            dictionary[next_comp] = next
            next += 1
            word = char
    if word:
        output.append(dictionary[word])
    return output

def lzw_decompress(compressed):
    dictionary = {i: chr(i) for i in range(256)}
    next= 256
    word = ""
    output = []
    for code in compressed:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next:
            entry = word + word[0]
        else:
            raise ValueError("Bad compressed code: {}".format(code))
        output.append(entry)
        if word:
            dictionary[next] = word + entry[0]
            next += 1
        word = entry
    return ''.join(output)



