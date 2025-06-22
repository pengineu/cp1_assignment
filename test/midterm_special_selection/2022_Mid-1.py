def fisherman(fish, gumul):
    fish_list = [0]
    for m in range(11 - gumul):
        for n in range(11 - gumul):
            fish_count = 0
            fish_repo = fish.copy()
            for i in range(gumul + 1):
                i = i + m
                for j in range(gumul + 1):
                    j = j + n
                    while [i, j] in fish_repo:
                        fish_count += 1
                        fish_repo.remove([i, j])
            fish_list.append(fish_count)
    return max(fish_list)

print(fisherman([[ 1, 1],
       [ 2, 4],
       [ 1, 9],
       [ 7, 3],
       [ 6, 7],
       [ 8, 8],
       [ 7, 9], [10, 10], [8, 9]],

3))
