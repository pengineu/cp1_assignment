import numpy as np


class Function:
    def __init__(self, func):
        self.func=func

    def get(self, x):
        try:
            return eval(self.func[2:])
        except:
            return eval("math." + (self.func[2:]))

class Integral(Function):
    def get(self, a, b, h):
        result = 0
        for i in np.arange(a, b, h):
            result += h * (super().get(i) + super().get(i + h)) / 2
        return result


i=Integral("y=log(x)")
print(i.get(0.001, 10, 0.001))
k= Integral("y=x**2")
print(k.get(0, 2, 0.1))