def collatz(n: int) -> list:
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        result.append(n)
    return max(result)


print(collatz(3))