def decode(rle: str) -> str:
    idx = 0
    result = []
    while idx <= len(rle) - 1:
        try:
            repeat = int(rle[idx + 1])
            result.append(rle[idx] * repeat)
            idx += 2
        except:
            result.append(rle[idx])
            idx += 1
    return ''.join(result)

print(decode("w3navercom"))