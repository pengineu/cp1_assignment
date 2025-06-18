class Function:
    def __init__(self, func):
        self.func=func

    def get(self, x):
        return eval(self.func.split("y=")[1])

class Differential(Function):
    h = 0.00000001
    def get(self, x):
        return (Function.get(self, x + self.h) - Function.get(self, x - self. h)) / (2 * self.h)

d=Differential("y=2*x")
r=d.get(10)
print(r)