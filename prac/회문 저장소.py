class palindrome:
    def __init__(self):
        self.li = []

    def check(self, string):
        while len(string) >= 1:
            if string[0] == string[-1]:
                string = string[1:-1]
            else:
                return
        self.li.append("T")

    def __str__(self):
        return str(len(self.li))

p=palindrome()

p.check('LEVEL')
p.check('TOOTH')
p.check('RACECAR')

print(p)