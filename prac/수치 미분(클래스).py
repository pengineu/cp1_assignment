import math


class Function:
    def __init__(self, func):
        self.func=func

    def get(self, x):
        try:
            return eval(self.func.split("y=")[1])
        except:
            return eval("math." + self.func.split('y=')[1])

class Differential(Function):
    h = 0.00000001

    def get(self, x):
        return (Function.get(self, x + self.h) - Function.get(self, x)) / self.h

d=Differential("y=log(x)")
r=d.get(2)
print(r)