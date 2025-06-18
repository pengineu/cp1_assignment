import pandas as pd
import numpy as np


def max(df, attribute):
    return round(np.max(df[attribute]), 4)