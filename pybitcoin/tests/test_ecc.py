from pybitcoin.ecc import FieldElement, EllipticCurve, Point
import unittest


class ECCTest(unittest.TestCase):
    prime = 223
    a = FieldElement(num=0, prime=prime)
    b = FieldElement(num=7, prime=prime)
    curve = EllipticCurve(a=a, b=b)

    def test_on_curve(self):
        valid_points = ((192, 105), (17, 56), (1, 193))
        invalid_points = ((200, 119), (42, 99))

        for x_coord, y_coord in valid_points:
            x = FieldElement(num=x_coord, prime=self.prime)
            y = FieldElement(num=y_coord, prime=self.prime)
            Point(x=x, y=y, curve=self.curve)

        for x_coord, y_coord in invalid_points:
            x = FieldElement(num=x_coord, prime=self.prime)
            y = FieldElement(num=y_coord, prime=self.prime)
            with self.assertRaises(ValueError):
                Point(x=x, y=y, curve=self.curve)

    def test_add(self):
        additions = (
            (170, 142, 60, 139, 220, 181),
            (47, 71, 17, 56, 215, 68),
            (143, 98, 76, 66, 47, 71),
            (192, 105, 17, 56, 170, 142),
            (47, 71, 117, 141, 60, 139)
        )

        for x1_raw, y1_raw, x2_raw, y2_raw, x3_raw, y3_raw in additions:
            x1 = FieldElement(num=x1_raw, prime=self.prime)
            y1 = FieldElement(num=y1_raw, prime=self.prime)
            p1 = Point(x=x1, y=y1, curve=self.curve)

            x2 = FieldElement(num=x2_raw, prime=self.prime)
            y2 = FieldElement(num=y2_raw, prime=self.prime)
            p2 = Point(x=x2, y=y2, curve=self.curve)

            x3 = FieldElement(num=x3_raw, prime=self.prime)
            y3 = FieldElement(num=y3_raw, prime=self.prime)
            p3 = Point(x=x3, y=y3, curve=self.curve)

            self.assertEqual(p1 + p2, p3)


if __name__ == '__main__':
    unittest.main()
