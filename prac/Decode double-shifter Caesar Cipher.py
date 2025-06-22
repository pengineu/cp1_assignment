def caesar(Shifter: list, Ciper: str) -> str:
    shift = Shifter * (len(Ciper)*2)
    result = []
    idx = 0
    for i in Ciper:
        shifted = ord(i) - shift[idx]
        if shifted < 97:
            shifted += 26
        result.append(chr(shifted))
        idx += 1
    return ''.join(result)

print(caesar([3, 5], "ffhxdw"))