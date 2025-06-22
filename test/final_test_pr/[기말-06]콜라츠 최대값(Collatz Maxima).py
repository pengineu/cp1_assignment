def collatz(n: int) -> int:
    li = [n]
    while n != 1:
        if n % 2:
            n = 3*n + 1
            li.append(n)
        else:
            n = n // 2
            li.append(n)
    max_ = li.pop(li.index(max(li)))
    next_max = max(li)
    return max_ - next_max

print(collatz(1))