import numpy as np

def track(fields: list, powers: list) -> list:
    idx = 0
    np_fields = np.array(fields)
    compare = np.zeros(np.shape(np_fields[0]))
    for field in fields:
        np_field = np.array(field)
        compare += abs(np_field - powers[idx])
        idx += 1
    real_compare = compare
    smallest_colum = []
    for i in real_compare:
        smallest = 1000000000000000000000000000000000000000000000000000000000000000000000000000
        idx = 0
        for m in i:
            if m < smallest:
                smallest = m
                smallest_idx = idx
            idx += 1
        smallest_colum.append(smallest_idx)
    row_idx = 0
    smallest = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    for i in smallest_colum:
        m = real_compare[row_idx][i]
        if m < smallest:
            smallest = m
            row = row_idx
            colum = i
        row_idx += 1
    return [row, colum]

fields=[[[0, 0.1, 0.2, 0.1, 0],
         [0.1, 0.2, 0.5, 0.2, 0.1],
         [0.3, 0.6, 1, 0.6, 0.3],
         [0.1, 0.2, 0.5, 0.2, 0.1],
         [0, 0.1, 0.2, 0.1, 0]],
        [[1, 0.7, 0.4, 0.2, 0.1],
         [0.8, 0.5, 0.3, 0.1, 0],
         [0.4, 0.2, 0.1, 0, 0],
         [0.1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]],
        [[0.1, 0.3, 0.5, 0.9, 1],
         [0, 0.1, 0.3, 0.8, 0.9],
         [0, 0, 0.1, 0.6, 0.7],
         [0, 0, 0, 0.3, 0.4],
         [0, 0, 0, 0, 0.1]]]

powers=[0.099, 0.702, 0.299]

print(track(fields, powers))