import unittest
from decimal import Decimal

import matpak
from matpak.errors import MatrixDimensionInvalid


class TestMatrix(unittest.TestCase):
    def test_mat_invalid_dim(self):
        with self.assertRaises(MatrixDimensionInvalid):
            matpak.Matrix(-1, 1024)

        with self.assertRaises(MatrixDimensionInvalid):
            matpak.Matrix(1024, 0)

        with self.assertRaises(MatrixDimensionInvalid):
            matpak.Matrix(0, -2134)

    def test_mat_shape(self):
        # matrix with initial matrix values
        mat_01: matpak.Matrix = matpak.Matrix(3, 3, [
            [Decimal(1.0), Decimal(2.0), Decimal(3.0)],
            [Decimal(4.0), Decimal(5.0), Decimal(6.0)],
            [Decimal(7.0), Decimal(8.0), Decimal(9.0)],
        ])

        # zero initialized matrix
        mat_02: matpak.Matrix = matpak.Matrix(1024, 2)

        self.assertTupleEqual(mat_01.shape, (3, 3))
        self.assertTupleEqual(mat_02.shape, (1024, 2))

    def test_mat_raw(self):
        raw_mat = [
            [Decimal(1.0), Decimal(2.0), Decimal(3.0)],
            [Decimal(4.0), Decimal(5.0), Decimal(6.0)],
            [Decimal(7.0), Decimal(8.0), Decimal(9.0)],
        ]

        mat_01: matpak.Matrix = matpak.Matrix(3, 3, raw_mat)
        mat_02: matpak.Matrix = matpak.Matrix(1024, 1024)

        self.assertListEqual(mat_01.raw, raw_mat)
        self.assertListEqual(mat_02.raw, [[Decimal(0.0)] * 1024 for _ in range(1024)])

    def test_mat_set(self):
        mat: matpak.Matrix = matpak.Matrix(3, 3)

        with self.assertRaises(ValueError):
            mat.set(33, 13, Decimal(91.0))

        with self.assertRaises(ValueError):
            mat.set(-1, 1, Decimal(344.0))

        for i in range(3):
            mat.set(i, i, Decimal(1.0))

        self.assertListEqual(mat.raw, [
            [Decimal(1.0), Decimal(0.0), Decimal(0.0)],
            [Decimal(0.0), Decimal(1.0), Decimal(0.0)],
            [Decimal(0.0), Decimal(0.0), Decimal(1.0)]
        ])

    def test_mat_get(self):
        mat: matpak.Matrix = matpak.Matrix(32, 32)
        mat.set(15, 15, Decimal(0.0000000000005))

        self.assertAlmostEqual(mat.get(15, 15), Decimal(0.0000000000005), 32)
        self.assertNotAlmostEqual(mat.get(15, 15), Decimal(0.00000000000005), 32)

    def test_mat_multiply(self):
        mat_01 = matpak.Matrix(3, 3, [
            [Decimal(1.0), Decimal(2.0), Decimal(3.0)],
            [Decimal(4.0), Decimal(5.0), Decimal(6.0)],
            [Decimal(7.0), Decimal(8.0), Decimal(9.0)],
        ])

        mat_02 = matpak.Matrix(3, 2, [
            [Decimal(10.0), Decimal(11.0)],
            [Decimal(12.0), Decimal(13.0)],
            [Decimal(14.0), Decimal(15.0)]
        ])

        vec_01 = matpak.Vector(3, [Decimal(10.0), Decimal(11.0), Decimal(12.0)])

        mat_03 = mat_01.multiply(mat_02)
        mat_04 = mat_01.multiply_col_major(mat_02)

        vec_02 = mat_01.multiply(vec_01)
        vec_03 = mat_01.multiply_col_major(vec_01)

        self.assertListEqual(mat_03.raw, [
            [Decimal(76.0), Decimal(82.0)],
            [Decimal(184.0), Decimal(199.0)],
            [Decimal(292.0), Decimal(316.0)]
        ])

        self.assertListEqual(mat_04.raw, [
            [Decimal(76.0), Decimal(82.0)],
            [Decimal(184.0), Decimal(199.0)],
            [Decimal(292.0), Decimal(316.0)]
        ])

        self.assertEqual(vec_02.raw, [Decimal(68.0), Decimal(167.0), Decimal(266.0)])
        self.assertEqual(vec_03.raw, [Decimal(68.0), Decimal(167.0), Decimal(266.0)])


if __name__ == "__main__":
    unittest.main()
