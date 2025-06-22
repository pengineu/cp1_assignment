import math
import numpy as np

class Function:
    def __init__(self, func):
        self.func=func

    def get(self, x):
        equ = self.func.split("=")[1]
        if "log" in equ:
            return eval(equ.replace("log", "math.log"))
        else:
            return eval(equ)

class Integral(Function):
    def get(self, a, b, h):
        sum_ = 0
        for x in np.arange(a, b, h):
            sum_ += h * (super().get(x) + super().get(x+h)) / 2
        return sum_

i= Integral("y=x**2")
r=i.get(0, 2, 0.1)
print(r)