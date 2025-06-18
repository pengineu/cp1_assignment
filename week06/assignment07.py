def collatz(arg):
    li = [arg]
    while arg != 1:
        if arg % 2 == 0:
            arg = arg / 2
        else:
            arg = arg*3 + 1
        li.append(arg)
    max_1 = max(li)
    li.remove(max_1)
    max_2 = max(li)
    return int(max_1 - max_2)



