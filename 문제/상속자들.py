class Animal:
    def __init__(self, age, name):
        self.age=age
        self.name=name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def __str__(self):
        return "<"+self.name+":"+str(self.age)+">"

class Cat(Animal):
    def speak(self):
        return print("Meow")

    def feature(self):
        return "Cute"

    def __str__(self):
        return "<" + self.name + ":" + str(self.age) + ":Cute>"

c=Cat(5, "Doongsil")
print(c.get_age())
print(c.get_name())
print(c.feature())
c.speak()
print(c)