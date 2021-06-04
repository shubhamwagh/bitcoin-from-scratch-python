from pybitcoin.ecc import Point, EllipticCurve
import unittest


class EllipticCurveTest(unittest.TestCase):
    def test_eq(self):
        curve = EllipticCurve(a=5, b=7)
        self.assertEqual(curve, curve)

    def test_ne(self):
        curve_1 = EllipticCurve(a=5, b=7)
        curve_2 = EllipticCurve(a=7, b=11)
        self.assertNotEqual(curve_1, curve_2)


class PointTest(unittest.TestCase):
    curve = EllipticCurve(a=5, b=7)

    def test_ne(self):
        a = Point(x=3, y=-7, curve=self.curve)
        b = Point(x=18, y=77, curve=self.curve)
        self.assertTrue(a != b)
        self.assertFalse(a != a)

    def test_add0(self):
        a = Point(x=None, y=None, curve=self.curve)
        b = Point(x=2, y=5, curve=self.curve)
        c = Point(x=2, y=-5, curve=self.curve)
        self.assertEqual(a + b, b)
        self.assertEqual(b + a, b)
        self.assertEqual(b + c, a)

    def test_add1(self):
        a = Point(x=3, y=7, curve=self.curve)
        b = Point(x=-1, y=-1, curve=self.curve)
        self.assertEqual(a + b, Point(x=2, y=-5, curve=self.curve))

    def test_add2(self):
        a = Point(x=-1, y=-1, curve=self.curve)
        self.assertEqual(a + a, Point(x=18, y=77, curve=self.curve))


if __name__ == '__main__':
    unittest.main()
