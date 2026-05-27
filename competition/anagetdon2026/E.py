# def strength(peoples: list, N):
#     if N == 1:
#         return peoples[0], 0
#     sum_ = sum(peoples)
#     div = (sum_ / 2) #힘 합을 2로 나누어 반올림
#
#     plus_sum = 0
#     for i in range(N):
#         plus_sum += peoples[i]
#         diff = plus_sum - div
#         if is_plus(diff):                               #차이가 최소가 되는 지점
#             diff = abs(plus_sum - (sum_ - plus_sum))
#             last_sum = plus_sum - peoples[i]
#             last_diff = abs(sum_ - last_sum - last_sum)
#             if i == 0:
#                 return sum_ - last_sum - last_sum, i
#             if last_diff <= diff:                       # +가 되는 지점에서 이전 차이가 더 작다면
#                 last_last_diff = abs(sum_ - plus_sum - peoples[i-1] - plus_sum - peoples[i-1])
#
#                 if last_diff == last_last_diff:         #이전 차이가 같으면
#                     while last_diff == last_diff:
#                         if i == 0:
#                             return sum_ - last_sum - last_sum, i
#                         last_last_diff = abs(sum_ - plus_sum - peoples[i-1] - plus_sum - peoples[i-1])
#                         i -= 1                          #이전으로 감
#                     return sum_ - last_sum - last_sum, i
#                 return sum_ - last_sum - last_sum , i-1      #이전 차이 반환
#             return sum_ - plus_sum, i
#
# def is_plus(n):
#     if n >= 0:
#         return True
#     return False

def strength(peoples: list, N):
    plus_sum = 0
    sum_ = sum(peoples)
    diff_list = []

    for i in peoples:
        plus_sum += i
        diff_list.append(abs(plus_sum - (sum_ - plus_sum)))

    min_ = min(diff_list)
    idx = diff_list.index(min_)
    return min_, idx

if __name__ == "__main__":
    N = int(input())
    people = list(map(int, input().split()))

    s, i = strength(people, N)
    print(f"{s} {i}")