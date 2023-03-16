import math


class Shape:
    def __init__(self, name, color, filled):
        self.name = str(name)
        self.color = str(color)
        self.filled = bool(filled)

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, name, color, filled, radius):
        super().__init__(name, color, filled)
        self.radius = float(radius)

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, name, color, filled, width, length):
        super().__init__(name, color, filled)
        self.width = float(width)
        self.length = float(length)

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, name, color, filled, side):
        super().__init__(name, color, filled, side, side)


circle = Circle("circle", "blue", False, 4)
rectangle = Rectangle("rectangle", "white", True, 2, 3)
square = Square("square", "red", True, 5)

print(circle.get_area())
print(circle.get_perimeter())
print(rectangle.get_perimeter())
print(rectangle.get_area())
print("square perm", square.get_perimeter())
print(square.get_area())
