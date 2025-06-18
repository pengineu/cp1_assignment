import pandas as pd
import numpy as np

def outlier(df):
    std , mean = np.std(df), np.mean(df)
    return abs(df - mean) >= std

print(outlier(pd.DataFrame(([4, 1, 10], [4.2, 1.2, 14], [3.8, 0, 1000], [-4, 0.9, 9]))))