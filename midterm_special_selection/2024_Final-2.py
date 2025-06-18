# def castle(Rc: float, args: list) -> bool:
#     import math
#     range_ = Rc * 2 * math.pi
#     if max(args) > 2 * Rc:
#         return True
#     else:
#         for arg in args:
#             theta_half = arg / (2*Rc)
#             theta = 2 * math.asin(theta_half)
#             shild_range = Rc * (2 * theta)
#             range_ -= shild_range
#         if range_ > 0:
#             return False
#         else:
#             return True


def castle(Rc: float, R: list) -> bool:
    import math
    if (Rc * 2) < max(R):
        return True
    else:
        circle = 2 * math.pi
        for r in R:
            circle -= 2 * math.acos(1 - (r**2 / (2 * Rc**2)))
        return circle <= 0

print(castle(101.0,
             [10.0, 20.0, 15.0, 5.0, 1.0, 60.0, 100.0, 11.0, 14.0, 12.0, 15.0]))