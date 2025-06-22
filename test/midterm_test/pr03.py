# def triangular_walk(n):
#     r = 1
#     s = 2
#     while r < n:
#         n -= r
#         r += 1
#     li1 = list(range(1, r +1))
#     li2 = list(range(r, 0, -1))
#
#     if r % 2:
#         li1, li2 = li2, li1
#     return li1[n - 1], li2[n - 1]


def triangular_walk(n: int) -> tuple:
    count = 1
    while n > count:
        n -= count
        count += 1
    pos1_list = list(range(1, count + 1))
    pos2_list = list(range(count, 0, -1))
    if count % 2:
        pos1_list, pos2_list = pos2_list, pos1_list
    pos1, pos2 = pos1_list[n - 1], pos2_list[n - 1]
    return pos1, pos2

print(triangular_walk(100))