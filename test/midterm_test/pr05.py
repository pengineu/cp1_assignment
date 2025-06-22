# def sliding_window(li, ran):
#     result = []
#     for k in range(len(li) - ran + 1):
#         idx = k
#         repo =[]
#         for i in range(ran):
#             repo.append(li[idx])
#             idx += 1
#         result.append(sum(repo))
#     return result

def sliding_window(vec: list, r: int) -> list:
    repeat = len(vec) - r
    result = []
    sum_ = 0
    for i in range(r):
        sum_ += vec[i]
    result.append(sum_)
    for i in range(repeat):
        sum_ -= vec[i]
        sum_ += vec[r + i]
        result.append(sum_)
    return result

print(sliding_window([1,2,3,4,5,6,7,8,9]
,5))