from ecc import FieldElement

if __name__ == "__main__":
    f7 = FieldElement(3, 7)
    f11 = FieldElement(7, 11)
    print(f7)
    print(f11)
    print(f7 == f11)
