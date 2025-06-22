class math:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

m = math(10, 5)
print(m.add())
print(m.div())
print(m.mul())
print(m.sub())