def collatz(n: int) -> int:
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        result.append(n)
    return max(result)

def max_collatz(li: list) -> int:
    max_li = []
    for i in li:
        max_li.append(collatz(i))
    return li[max_li.index(max(max_li))]

print(max_collatz([5, 7, 13, 50]))