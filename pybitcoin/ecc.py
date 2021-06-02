from __future__ import annotations
from typing import Optional


class FieldElement:
    def __init__(self, num: int, prime: int) -> None:
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other: Optional[FieldElement, None]) -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other: Optional[FieldElement, None]) -> bool:
        return not (self == other)

    def __add__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')

        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')

        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')

        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent: int) -> FieldElement:
        wrapped_exponent = exponent % (self.prime - 1)
        num = pow(self.num, wrapped_exponent, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other: FieldElement) -> FieldElement:
        # Using Fermat's theorem : n^(p-1) % p = 1 for n > 0 and p being any prime number
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')

        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return self.__class__(num, self.prime)


class Point:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        if self.x is None and self.y is None:
            return
        if self.y ** 2 != self.x ** 3 + a * self.x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)

    def __eq__(self, other):
        return self.x == other.x and \
               self.y == other.y and \
               self.a == other.a and \
               self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format
                            (self, other))
        if self.x is None:
            # Handling infinity point case
            return other

        if other.x is None:
            # Handling infinity point case
            return self

        if self.x == other.x and self.y != other.y:
            # Handling vertical line case
            return self.__class__(None, None, self.a, self.b)

        if self.x != other.x:
            # Handling general slant line case with valid slope intersecting at a point
            slope = (other.y - self.y) / (other.x - self.x)
            result_x = pow(slope, 2) - self.x - other.x
            result_y = slope * (self.x - result_x) - self.y
            return self.__class__(result_x, result_y, self.a, self.b)

        if self == other and self.y == 0 * self.x:
            # Handling vertical tangent line at y=0
            return self.__class__(None, None, self.a, self.b)

        if self == other:
            # Handling general tangent line to elliptic curve intersecting at one point
            slope = (3 * pow(self.x, 2) + self.a) / (2 * self.y)
            x = pow(slope, 2) - 2 * self.x
            y = slope * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)
