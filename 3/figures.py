from math import pi

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

    def compare_area(self, other_shape):
        if self.area() > other_shape.area():
            return "Первая фигура имеет большую площадь, чем вторая."
        elif self.area() < other_shape.area():
            return "Первая фигура имеет меньшую площадь, чем вторая."
        else:
            return "Обе фигуры имеют одинаковую площадь."

    def compare_perimeter(self, other_shape):
        if self.perimeter() > other_shape.perimeter():
            return "Первая фигура имеет больший периметр, чем вторая."
        elif self.perimeter() < other_shape.perimeter():
            return "Первая фигура имеет меньший периметр, чем вторая."
        else:
            return "Обе фигуры имеют одинаковый периметр."

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


# example usage

square1 = Square(5)
print("Площадь квадрата:", square1.area())
print("Периметр квадрата:", square1.perimeter())


rect1 = Rectangle(8, 4)
print("Площадь прямоугольника:", rect1.area())
print("Периметр прямоугольника:", rect1.perimeter())

print(square1.compare_area(rect1))
