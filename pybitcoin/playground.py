from ecc import FieldElement, Point, EllipticCurve

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

    curve = EllipticCurve(a=5, b=7)
    p1 = Point(-1, 1, curve)
    p2 = Point(18, 77, curve)
    inf = Point(None, None, curve)
    print(p1 + p2)