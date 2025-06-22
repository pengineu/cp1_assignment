import numpy as np

def fisherman(fishs: np.array, net: int) -> int:
    max_ = 0
    for man_x in range(11):
        for man_y in range(11):
            fish_x = list(range(man_x, man_x+net+1))
            fish_y = list(range(man_y, man_y+net+1))
            catch = set((x, y) for x in fish_x for y in fish_y)
            max_ = max(howmany(fishs, catch), max_)
    return max_

def howmany(fishs, catch):
    cnt = 0
    for fish in fishs:
        fish = tuple(fish)
        if fish in catch:
            cnt += 1
    return cnt

print(fisherman([[ 1, 1],
           [ 1, 1],
           [ 1, 1],
           [ 2, 4],
           [ 1, 9],
           [ 7, 3],
           [ 6, 7],
           [ 8, 8],
           [ 7, 9]],

0))