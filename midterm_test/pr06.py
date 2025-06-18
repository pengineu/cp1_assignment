def spiral_product(A: list, B: list) -> list:
    result = []
    B_list = []
    A_repo = []
    rang = len(A)
    while len(B) > 1:
        repo_3 = []
        repo_4 = []
        repo_last = []
        repeat = len(B) - 1
        for i in range(repeat):
            B_list.append(B[0][i])
        for i in range(repeat):
            B_list.append(B[i][-1])
        for i in range(1, repeat + 1):
            repo_3.append(B[-1][i])
        repo_3 = reversed(repo_3)
        B_list.extend(repo_3)
        for i in range(1, repeat + 1):
            repo_4.append(B[i][0])
        repo_4 = reversed(repo_4)
        B_list.extend(repo_4)
        B.remove(B[0])
        B.remove(B[-1])
        for j in range(repeat - 1):
            repo_last.append(B[j][1:-1])
        B = repo_last.copy()
    if len(B) == 1:
        B_list.append(B[0][0])
    B = B_list.copy()
    for i in range(len(A)):
        for j in range(len(A)):
            A_repo.append(A[i][j])
    A = A_repo.copy()
    idx = 0
    for j in range(rang):
        result_repo = []
        for i in range(rang):
            result_repo.append((A[idx] * B[idx]))
            idx += 1
        result.append(result_repo)
    return result


spiral_product([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
], [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
])