def only_integer(data: list) -> list:
    return list(filter(lambda x: x == int(x), data))

print(only_integer([1, 2.2, 4.0]))