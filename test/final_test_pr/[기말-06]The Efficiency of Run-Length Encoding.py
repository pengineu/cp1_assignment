def efficiency(text: str) -> int:
    result = ""
    leng = len(text)
    while text:
        word = text[0]
        cnt = 0
        for i in text:
            if i == word:
                cnt += 1
            if i != word or i == text[-1] and cnt == len(text):
                text = text[cnt:]
                break
        if cnt == 1:
            result += word
        else:
            result += f"{word}{cnt}"
    return len(result) / leng

print(efficiency("aaaabbbb"))