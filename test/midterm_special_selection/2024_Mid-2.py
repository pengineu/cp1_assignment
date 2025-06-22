# def parity(arg):
#     import math
#     if arg > 0:
#         n = int(math.log(arg)/math.log(2))
#     else:
#         return True
#     par = 0
#     while n >= 0:
#         if arg - 2**n >= 0:
#             arg -= 2 ** n
#             par += 1
#         n -= 1
#     return par % 2 == 0

def parity(n: int) -> bool:
    return bin(n)[2:].count("1") % 2 == 0