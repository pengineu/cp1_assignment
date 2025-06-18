def caesar(arg1: list, arg2: str) -> str:
    import collections
    li = collections.deque(arg2)
    st = []

    while len(st) != len(arg2):
        st.append(ord(li.popleft()) - arg1[0])
        st.append(ord(li.popleft()) - arg1[1])
    number = []

    for i in st:
        if i < 97:
            i += 26
        number.append(i)

    result = ''.join(list(map(chr, number)))

    return result

print(caesar([13, 25],
             'qnbmtrvk'))