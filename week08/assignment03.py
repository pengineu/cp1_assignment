class integer:
    def __init__(self, x):
        self.x = int(x)

    def __add__(self, other):
        return self.x + int(other)

    def __sub__(self, other):
        return self.x - int(other)

i=integer(1.5)

i+1.7
i-0.1