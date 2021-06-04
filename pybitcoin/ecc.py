from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


class FieldElement:
    """
    Implementation of Finite Field elements and operations
    """
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


@dataclass
class EllipticCurve:
    """
    Points on the elliptic curve satisfy y^2 = x^3 + a*x + b.
    """
    a: Optional[int, FieldElement]
    b: Optional[int, FieldElement]

    def __repr__(self) -> str:
        if self.a == 0:
            return "Elliptic Curve: y^2 = x^3 + {}".format(self.b)
        elif self.b == 0:
            return "Elliptic Curve: y^2 = x^3 + {}x".format(self.a)
        else:
            return "Elliptic Curve: y^2 = x^3 + {}x + {}".format(self.a, self.b)

    def __eq__(self, other: EllipticCurve) -> bool:
        return self.a == other.a and \
               self.b == other.b

    def __ne__(self, other: EllipticCurve) -> bool:
        return not (self == other)


class Point:
    """ An integer point (x,y) on a Curve """
    def __init__(self, x: Optional[int, None, FieldElement], y: Optional[int, None, FieldElement],
                 curve: EllipticCurve):
        self.x = x
        self.y = y
        self.curve = curve
        if self.x is None and self.y is None:
            return
        if self.y ** 2 != self.x ** 3 + self.curve.a * self.x + self.curve.b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))

    def __repr__(self) -> str:
        if self == self._INF:
            return 'Point(infinity)_curve_{}_{}'.format(self.curve.a, self.curve.b)
        else:
            return 'Point({},{})_curve_{}_{}'.format(self.x, self.y, self.curve.a, self.curve.b)

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and \
               self.y == other.y and \
               self.curve == other.curve

    def __ne__(self, other: Point) -> bool:
        return not (self == other)

    def __add__(self, other: Point) -> Point:
        if self.curve != other.curve:
            raise TypeError('Points {}, {} are not on the same curve'.format
                            (self, other))
        if self == self._INF:
            # Handling infinity point case
            # P + 0 = P
            return other

        if other == self._INF:
            # Handling infinity point case
            # 0 + P = P
            return self

        if self.x == other.x and self.y != other.y:
            # Handling vertical line case
            # P + (- P) = 0
            return self._INF

        if self == other and self.y == 0 * self.x:
            # Handling vertical tangent line at y=0
            return self._INF

        if self.x == other.x:  # (self.y = other.y is guaranteed too per "vertical line case" check)
            # Handling general tangent line intersecting at one point
            slope = (3 * pow(self.x, 2) + self.curve.a) / (2 * self.y)
        else:
            # Handling general slant line case with valid slope intersecting at any three points
            slope = (other.y - self.y) / (other.x - self.x)
        result_x = pow(slope, 2) - self.x - other.x
        result_y = slope * (self.x - result_x) - self.y
        return self.__class__(result_x, result_y, self.curve)

    @property
    def _INF(self) -> Point:
        # Infinity point
        return self.__class__(None, None, self.curve)
