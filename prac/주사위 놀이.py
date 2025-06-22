def dice(d1, d2, d3):
    if d1 != d2 and d2 != d3 and d1 != d3:
        return max(d1, d2, d3) * 100
    elif d1 == d2 and d2 == d3:
        return 10000 + d1*1000
    else:
        li = sorted([d1, d2, d3])
        return 1000 + li[1]*100

print(dice(3, 3, 6))