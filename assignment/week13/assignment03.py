import numpy as np


def outlier(arr):
    std = np.std(arr)
    m = np.mean(arr)
    return arr >= std + m

print(outlier([0.5, 0.3, 0.1, 0.2, 10.0]))