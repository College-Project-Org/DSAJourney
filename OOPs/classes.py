class Square:
    # constructor
    def __init__(self, side):
        self.side = side

    def perimiter(self, cost=None, material=None):
        if material:
            print(material)
        return (self.side * 4) * cost

    def area(self, *args, **kwargs):
        return self.side * self.side

    def estate_name():
        return "Swarnabhoomi"


# encapsulation
# abstraction
# polymorphism
# inheritance


square1 = Square(10)
square2 = Square(20)
print("Perimeter", square2.perimiter(cost=25))
print("Area:", square2.area())
