def vigenere(sent: str, key: str) -> str:
    sentord = [ord(i) for i in sent]
    keyord = [ord(i) - 97 for i in key]
    result = []
    for i in range(len(sentord)):
        word = sentord[i] + keyord[i]
        if word > 122:
            word -= 26
        result.append(chr(word))
    return ''.join(result)

print(vigenere('hello','abcde'))