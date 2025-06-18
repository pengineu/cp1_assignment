def unique(arg1:list, arg2:list)->set:
    arg1, arg2 = set(arg1), set(arg2)
    return (arg1 | arg2) - (arg1 & arg2)

print(unique([1, 2, 3], [3, 4, 5, 6]))