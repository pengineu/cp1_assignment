class Function:
    def __init__(self, func):
        self.func=func

    def get(self, x):
        return eval(self.func.split("y=")[1])


class Configurable_Function(Function):
    def set(self, f):
        self.func = f

f=Configurable_Function("y=2*x")
r=f.get(10)
print(r)

f.set("y=x")
r=f.get(10)
print(r)