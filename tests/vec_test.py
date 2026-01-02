import unittest
from decimal import Decimal

import matpak
from matpak.errors import VectorDimensionInvalid


class TestVector(unittest.TestCase):
    def test_vec_invalid_dim(self):
        with self.assertRaises(VectorDimensionInvalid):
            matpak.Vector(-1)

        with self.assertRaises(VectorDimensionInvalid):
            matpak.Vector(0)

    def test_vec_shape(self):
        # vector with initial vector values
        vec_01: matpak.Vector = matpak.Vector(3, [Decimal(1.0), Decimal(2.0), Decimal(3.0)])

        # zero initialized vector
        vec_02: matpak.Vector = matpak.Vector(1024)

        self.assertTupleEqual(vec_01.shape, (3, 1))
        self.assertTupleEqual(vec_02.shape, (1024, 1))

    def test_vec_raw(self):
        raw_vec = [Decimal(1.0), Decimal(2.0), Decimal(3.0)]

        vec_01: matpak.Vector = matpak.Vector(3, raw_vec)
        vec_02: matpak.Vector = matpak.Vector(1024)

        self.assertListEqual(vec_01.raw, raw_vec)
        self.assertListEqual(vec_02.raw, [Decimal(0.0) for _ in range(1024)])

    def test_vec_set(self):
        vec: matpak.Vector = matpak.Vector(3)

        with self.assertRaises(ValueError):
            vec.set(33, Decimal(91.0))

        with self.assertRaises(ValueError):
            vec.set(-1, Decimal(344.0))

        for i in range(3):
            vec.set(i, Decimal(1.0))

        self.assertListEqual(vec.raw, [Decimal(1.0), Decimal(1.0), Decimal(1.0)])

    def test_vec_get(self):
        vec: matpak.Vector = matpak.Vector(32)
        vec.set(15, Decimal(0.0000000000005))

        self.assertAlmostEqual(vec.get(15), Decimal(0.0000000000005), 32)
        self.assertNotAlmostEqual(vec.get(15), Decimal(0.00000000000005), 32)

    def test_vec_multiply(self):
        vec_01 = matpak.Vector(3, [Decimal(1.0), Decimal(2.0), Decimal(3.0)])
        mat_01 = matpak.Matrix(1, 3, [
            [Decimal(10.0), Decimal(11.0), Decimal(12.0)]
        ])

        mat_02 = vec_01.multiply(mat_01)

        self.assertListEqual(mat_02.raw, [
            [Decimal(10.0), Decimal(11.0), Decimal(12.0)],
            [Decimal(20.0), Decimal(22.0), Decimal(24.0)],
            [Decimal(30.0), Decimal(33.0), Decimal(36.0)],
        ])


if __name__ == "__main__":
    unittest.main()
