import pandas as pd
import numpy as np

def sinmax(df):
    df = pd.DataFrame(df)
    df = df.apply(np.sin)
    return df.max(axis=1)

print(sinmax(([5, 6, 2], [7, 3, 10])))