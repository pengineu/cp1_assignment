def fifo(current_data: int, new_data: str) -> int:
    current_bin = bin(current_data)[2:]
    current_bin = "0"*(8-len(current_bin)) + current_bin
    new_bin = (current_bin + new_data)[len(new_data):]
    up = 7
    result = 0
    for i in new_bin:
        result += int(i) * 2**up
        up -= 1
    return result

print(fifo(1, "010"))