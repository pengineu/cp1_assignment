N = int(input())

bingo_table = [[i*N + j+1 for j in range(N)] for i in range(N)]
bingo = False

while not bingo:
    ans = int(input())
    ans_i = (ans - 1) // N
    ans_j = (ans - 1) % N
    bingo_table[ans_i][ans_j] = 0
    for i in range(N):
        sum_ = 0
        for j in range(N):
            sum_ += bingo_table[i][j]
        if not sum_:
            bingo = True
            break
        sum_ = 0
        for j in range(N):
            sum_ += bingo_table[j][i]
        if not sum_:
            bingo = True
            break
    sum_ = 0
    for i in range(N):
        sum_ += bingo_table[i][i]
    if not sum_:
        bingo = True
        break
    sum_ = 0
    for i in range(N):
        sum_ += bingo_table[i][N-i-1]
    if not sum_:
        bingo = True
        break


if bingo:
    print("bingo!")