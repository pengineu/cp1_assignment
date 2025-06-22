# def efficiency(word):
#     idx = 0
#     result = []
#     word_dict = {}
#     while idx < len(word):
#         word_dict[word[idx]] = word.count(word[idx])
#         idx += word_dict[word[idx]]
#     for i in word_dict:
#         if word_dict[i] == 1:
#             result.append(i)
#         else:
#             result.append(i)
#             result.append(word_dict[i])
#     press = ''.join(list(map(str, result)))
#     return (len(word) - len(press)) / len(word)

def efficiency(word):
    idx = 0
    result = []
    while idx < len(word):
        w = word[idx]
        equal = 1
        while idx != len(word) - 1 and w == word[idx+1]:
            equal += 1
            idx += 1
        idx += 1
        if equal == 1:
            result.append(w)
        else:
            result.append(w)
            result.append(str(equal))
    press = ''.join(result)
    return (len(word) - len(press)) / len(word)

print(efficiency("abababbbbb"))