from ecc import FieldElement

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
