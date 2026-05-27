# def stack_sort_count(N, stack):
#     max_ = 0
#
#     if N == 1:
#         return 0
#
#     for small, idxx in zip(stack, range(N)):
#         if small >= max_:
#             max_ = small
#         else:
#             for j, idx in zip(stack, range(N)):
#                 if j == small:
#                     return N - idx
#             minus = N - idxx
#             return N - minus
#     return 0

def stack_sort_count(N, stack):
    sorted_stack = sorted(stack)
    diff_start = N
    for i in range(N):
        if stack[i] != sorted_stack[i]:
            diff_start = i
            break
    return N - diff_start


if __name__ == "__main__":
    N = int(input())

    stack = list(map(int, input().split()))

    print(stack_sort_count(N, stack))