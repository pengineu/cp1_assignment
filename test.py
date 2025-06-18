def combination(n: list, r: int):
    repo = []
    lamda = [n.pop()]
    stack = []
    while repo[-1]
        new = n.pop()
        idx = 0
        for i in range(len(lamda)+1):
            for _ in range(idx):
                stack.append(lamda.pop())
            lamda.append(new)
            for _ in range(idx):
                lamda.append(stack.pop())
            idx += 1
            repo.append(lamda)