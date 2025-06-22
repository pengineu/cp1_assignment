import numpy as np

def standardization(nparr):
    mu = np.mean(nparr)
    sigma = np.mean((nparr - mu)**2)
    return (nparr - mu) / (sigma**0.5)



n = [100, 0]
n = np.array(n)

print(standardization(n))