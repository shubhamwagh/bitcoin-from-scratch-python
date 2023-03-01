from ecc import S256Point
if __name__ == "__main__":
    gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
    gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8

    G = S256Point(x=gx, y=gy)
    N = S256Point.N
    print(N * G)