def max_collatz(arg: list) -> int:
    max_value = []
    for i in arg:
        li = [i]
        if i == 1:
            li.append(1)
        else:
            while i != 1:
                if i % 2:
                    i = i * 3 + 1
                else:
                    i = i / 2
                li.append(i)
        max_value.append(max(li))
    return arg[max_value.index(max(max_value))]

print(max_collatz([2, 3, 4]))