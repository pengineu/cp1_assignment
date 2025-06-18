import math

distance, timelimit = [int(i) for i in input().split()]

n = int(input())

for i in range(n):
    shape, radius, rpm = input().split()
    shape = int(shape)
    radius = float(radius)
    rpm = float(rpm)
    pi = math.pi
    if shape > 2:
        theta = pi*2/shape
        if distance - (timelimit*rpm/60)*((radius*math.sin(theta)/(math.sin((pi-theta)/2)))*shape) <= 0:
            result = True
        else:
            result = False
    else:
        if distance - (timelimit*rpm/60)*pi*radius*2 <= 0:
            result = True
        else:
            result = False
    print(result)