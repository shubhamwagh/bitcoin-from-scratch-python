from ecc import FieldElement, Point, EllipticCurve

if __name__ == "__main__":
    a = FieldElement(0, 223)
    b = FieldElement(7, 223)
    curve = EllipticCurve(a, b)
    print(curve)
    p1 = Point(x=FieldElement(47, 223), y=FieldElement(71, 223), curve=curve)
    inf = Point(x=None, y=None, curve=curve)
