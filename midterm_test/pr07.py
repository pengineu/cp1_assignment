def divergence(a0: float, a1: float, i: float) -> float:
    if i == 1:
        return a1
    if i == 0:
        return a0
    else:
        return divergence(a0, a1, i-2) / divergence(a0, a1, i-1)

print(divergence(2, 1, 5))