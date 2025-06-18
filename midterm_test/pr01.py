def fifo(data, new):
    new_data = bin(data)[2:] + new
    if len(new_data) > 8:
        new_data = new_data[(len(new_data) - 8):]
    k = len(new_data) - 1
    sum_ = 0
    for i in new_data:
        if i == "1":
            sum_ +=  2 ** k
        k -= 1

    return sum_

print(fifo(51,
"111"))