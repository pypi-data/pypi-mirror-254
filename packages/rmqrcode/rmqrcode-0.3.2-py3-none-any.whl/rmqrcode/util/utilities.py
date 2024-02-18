def msb(n):
    return len(bin(n)) - 2


def to_binary(data, len):
    return bin(data)[2:].zfill(len)


def split_into_8bits(data):
    codewords = []
    while len(data) >= 8:
        codewords.append(data[:8])
        data = data[8:]
    if data != "":
        codewords.append(data.ljust(8, "0"))
    return codewords
