def norm(arg):
    square = map(lambda x: x**2, arg)
    su_m = 0
    for i in square:
        su_m += i

    result = su_m ** 0.5
    return round(result, 2)

norm([1, 2, 3])