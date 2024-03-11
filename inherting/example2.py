class Shape:
    def __init__(self, sides_length):
        self.sides_length = sides_length

class Square(Shape):
    def calculate_area(self):
        return self.sides_length[0] ** 2

class Rectangle(Shape):
        
    def calculate_area(self):
        return self.sides_length[0] * self.sides_length[1]

class Triangle(Shape):
    def is_valid(self):
        sides = sorted(self.sides_length)
        return sides[2] > sides[0] + sides[1]
    
    def sin(self):
        pass
    
    def cos(self):
        pass
    
    def tan(self):
        pass
    
    def ctg(self):
        pass
    
    
square1 = Square([6])
rectangle1 = Rectangle([4,7])
triangle1 = Triangle([4,6,3])

print(square1.calculate_area())
print(rectangle1.calculate_area())
print(triangle1.is_valid())