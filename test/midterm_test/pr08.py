def function(func='y=x', x=0):
    return eval(func.split('y=')[1])

def differential(func: str, x: float) -> float:
    h = 0.00000001
    return (function(func, (x + h)) - function(func, x)) / h

fun = [input() for i in range(2)]
print(differential(fun[0], float(fun[1])))