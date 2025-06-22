import numpy as np
import matplotlib.pyplot as plt


data = np.load(r"C:\Users\sinja\Desktop\이신재\코딩\컴프 과제\새 폴더\week13\Covid_Decided_Count.npy")
print(data)
bdata = np.log10(data)
expon = plt.hist(bdata)
print(plt.show())