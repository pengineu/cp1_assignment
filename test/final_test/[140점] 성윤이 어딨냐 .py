# import numpy as np
#
# def track(fields: list, powers: list) -> list:
#     idx = 0
#     np_fields = np.array(fields)
#     compare = np.zeros(np.shape(np_fields[0]))
#     for field in fields:
#         np_field = np.array(field)
#         compare += abs(np_field - powers[idx])
#         idx += 1
#     real_compare = compare
#     smallest_colum = []
#     for i in real_compare:
#         smallest = 1000000000000000000000000000000000000000000000000000000000000000000000000000
#         idx = 0
#         for m in i:
#             if m < smallest:
#                 smallest = m
#                 smallest_idx = idx
#             idx += 1
#         smallest_colum.append(smallest_idx)
#     row_idx = 0
#     smallest = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#     for i in smallest_colum:
#         m = real_compare[row_idx][i]
#         if m < smallest:
#             smallest = m
#             row = row_idx
#             colum = i
#         row_idx += 1
#     return [row, colum]


import numpy as np

def track(fields: list, powers: list) -> list:
    fields = np.array(fields)
    repo = np.zeros(np.shape(fields[0]))
    for power, field in zip(powers, fields):
        repo += abs(power - field)

    repo = list(repo)
    dic = {}
    idx = 0
    value = []
    for row in repo:
        row = list(row)
        dic[idx] = row.index(min(row))
        value.append(min(row))
        idx += 1

    min_ = 1000000
    for i in range(idx):
        if value[i] < min_:
            min_ = value[i]
            result = [i, dic[i]]
    return result

print(track([[[0.521, 0.836, 0.762, 0.644, 0.194],
              [0.767, 0.663, 1.0, 0.454, 0.424],
              [0.788, 0.973, 0.666, 0.454, 0.419],
              [0.706, 0.552, 0.417, 0.213, 0.38],
              [0.637, 0.324, 0.242, 0.277, 0.0]],
             [[0.239, 0.0, 0.338, 0.368, 0.478],
              [0.523, 0.919, 0.616, 0.455, 0.759],
              [0.478, 0.666, 0.705, 0.575, 0.714],
              [0.569, 1.0, 0.692, 0.842, 0.584],
              [0.226, 0.261, 0.782, 0.347, 0.996]],
             [[0.217, 0.583, 0.574, 0.76, 0.846],
              [0.448, 0.007, 0.635, 0.795, 0.123],
              [0.326, 0.62, 0.725, 1.0, 0.0],
              [0.762, 0.939, 0.667, 0.18, 0.457],
              [0.221, 0.431, 0.754, 0.185, 0.085]]],
            [0.42, 0.765, 0.13]
            ))