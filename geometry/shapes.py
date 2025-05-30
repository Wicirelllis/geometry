import math
from abc import ABC


class Shape(ABC):
    @property
    def area(self):
        'Area of the shape'
        raise NotImplemented


class Circle(Shape):
    def __init__(self, r: float):
        super().__init__()
        if r < 0.:
            raise ValueError('Radius must be non-negative.')
        self.r = r
    
    @property
    def area(self) -> float:
        return math.pi * self.r * self.r


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()
        if a < 0 or b < 0 or c < 0:
            raise ValueError('Edge length must be non-negative.')
        if a > b + c or b > c + a or c > a + b:
            raise ValueError('Edge lengths must satisfy triangle inequality.')
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
