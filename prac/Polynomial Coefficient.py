from collections import deque

def polynomial(string: str) -> str:
    li = string.split("+")
    sep = []
    dic = {}
    result = []
    for i in li:
        spt = i.split("-")
        sp = deque(spt)
        sep.append(sp.popleft())
        while sp:
            sep.append("-" + sp.popleft())
    for i in sep:
        if "x" not in i:
            continue
        if i[0] == "x":
            coe = "1"
        else:
            coe = i[0:i.index("x")]
            if coe == "-":
                coe = "-1"
            else:
                coe = coe[:-1]
        if "^" not in i:
            up = 1
        else:
            up = int(i[i.index("^") + 1:])
        dic[up] = coe
    if dic:
        max_up = max(dic)
        while max_up:
            if max_up in dic:
                result.append(dic[max_up])
            else:
                result.append("0")
            max_up -= 1
        return ','.join(result)
    else:
        return ''

print(polynomial("-6"))