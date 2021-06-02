from ecc import FieldElement, Point

if __name__ == "__main__":
    f7 = FieldElement(3, 13)
    f11 = FieldElement(7, 13)
    print(f7)
    print(f11)
    print(f7 + f11)
    print(f7 - f11)
    print(f7 * f11)
    print(f7 / f11)
    print(f7 ** -3)
    print(f7 != None)

    p1 = Point(-1, -1, 5, 7)
    p2 = Point(18, 77, 5, 7)
    inf = Point(None, None, 5, 7)
    print(p1 + p2)