# def quark(arg: list):
#     import math
#     li = list(map(math.sin, arg))
#     return arg[li.index(max(li))]
#
# print(quark([3.141592653589793, 1.5707963267948966, 0.7853981633974483, 2.356194490192345]))

def quark(location: list) -> float:
    import math
    probability = list(map(math.sin, location))
    return location[probability.index(max(probability))]

print(quark([3.141592653589793, 1.5707963267948966, 0.7853981633974483, 2.356194490192345]))