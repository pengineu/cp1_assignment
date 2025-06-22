class math:
    def __init__(self, x = 1, y = 1):
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

    def pow(self):
        return self.x ** self.y

    def root(self):
        return self.x ** (1/self.y)

m = math(2, 5)
print(m.add())
print(m.div())
print(m.mul())
print(m.sub())
print(m.pow())
print(m.root())