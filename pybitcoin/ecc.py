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
