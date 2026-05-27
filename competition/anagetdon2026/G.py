N = int(input())

work = [list(map(int, input().split())) for _ in range(N)]
li1 = []
li2 = []
for i in work:
    li1.append(work[0])
    li2.append(work[1])

sum_ = [sum(i) for i in work]

result = 0

for _ in range(N):
    max_ = max(li2)
    idx = li2.index(max_)
    result += li1[idx]
    result += li2[idx]
    li1.pop(idx)
    li2.pop(idx)