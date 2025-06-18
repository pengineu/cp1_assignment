import pandas as pd

def avg(args):
    args = pd.DataFrame(args)
    return args.mean(axis=1)

print(avg(([5, 6, 2], [7, 3, 10])))