# def missile(r, theta, v):
#     import math
#     theta = math.radians(theta)
#     return r * theta / (2 * v)


def missile(r, theta, v):
    import math
    radius = r / 2
    return (radius * ((theta * math.pi) / 180)) / v
print(missile(13, 30, 1))