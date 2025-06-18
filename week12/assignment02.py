def encrypt(x):
    return hex(abs(hash(str(x))))[2:]

def dont_steal_our_info(data: list) -> list:
    return list(map(encrypt, data))

print(dont_steal_our_info([1, 2]))