def fisherman(fish_list: list, net_size: int) -> int:
    max_fish = 0
    for m in range(11):
        for n in range(11):
            fish_count = len([fish for fish in fish_list
                              if fish[0] <= m + (net_size) and fish[0] >= m
                              and fish[1] <= n + (net_size) and fish[1] >= n])
            max_fish = max(max_fish, fish_count)

    return max_fish

print(fisherman([[ 1, 1],
                 [ 2, 4],
                 [ 1, 9],
                 [ 7, 3],
                 [ 6, 7],
                 [ 8, 8],
                 [ 7, 9]]

,5))