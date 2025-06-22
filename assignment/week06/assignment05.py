# A=input().split()
# B=input().split()
#
# result = []
#
# while A != [] and B != []:
#     result.append(A.pop(0))
#     result.append(B.pop(0))
#
#
# print(' '.join(result))

import numpy as np

AB = np.array([list(map(int, input().split())) for _ in range(2)]).T
for i in AB:
    print(*i, end=" ")