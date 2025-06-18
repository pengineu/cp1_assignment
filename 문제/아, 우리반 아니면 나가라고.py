class Class:
    def __init__(self, names):
        self.names = names

    def __str__(self):
        return ','.join(self.names)

    def check(self, name):
        if name in self.names:
            return True
        return False

c=Class(["박연진", "권민서", "신수림", "서주연"])
print(c)
print(c.check("박연진"))