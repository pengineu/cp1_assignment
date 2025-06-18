def caesar(N, code):
    result = []
    for i in code:
        ascii = ord(i)
        if ascii <= 96 + N:
            ascii = ascii + 26
        result.append(chr(ascii - N))
    return ''.join(result)

print(caesar(3, "fdhvdu"))