import math
from abc import ABC, abstractmethod
from typing import Union

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def is_right_angled(self) -> bool:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def is_right_angled(self) -> bool:
        return False

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны должны быть положительными числами")
        if max(sides) >= sum(sides) - max(sides):
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_angled(self, tolerance: float = 1e-6) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tolerance

def calculate_area(shape: Union[Circle, Triangle]) -> float:
    return shape.area()

def is_right_angled(shape: Union[Circle, Triangle]) -> bool:
    return shape.is_right_angled()
