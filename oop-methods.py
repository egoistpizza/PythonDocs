# ----- OOP-Methods ----- #

class Circle:

    # class object attribute
    pi = 3.14

    # constructor
    def __init__(self, radius = 1):
        self.radius = radius

    # instance methods
    def circumference(self):
        return 2 * self.pi * self.radius
    def zone(self):
        return self.pi * (self.radius ** 2)
    def changePi(self, newPi):
        self.pi = newPi

circle1 = Circle(7)
print(f'circle1 Çevre = {circle1.circumference()}, Alan = {circle1.zone()}')
circle1.changePi(3.14159)
print(f'circle1 Çevre = {circle1.circumference()}, Alan = {circle1.zone()}')