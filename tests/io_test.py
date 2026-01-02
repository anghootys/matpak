import unittest
from decimal import Decimal

import matpak
from matpak import Matrix, Vector
from matpak.errors import MatrixFileInvalid, VectorFileInvalid


class TestMatIOFuncs(unittest.TestCase):
    def test_imp_mat_file_fail_on_not_existed_file(self):
        with self.assertRaises(FileNotFoundError):
            matpak.imp_mat_file("unexisted_file.txt")

    def test_imp_mat_file_empty_line(self):
        with self.assertRaises(MatrixFileInvalid):
            matpak.imp_mat_file("tests/test_mat_01.txt")

    def test_imp_mat_file_contains_illegal_chars(self):
        with self.assertRaises(MatrixFileInvalid):
            matpak.imp_mat_file("tests/test_mat_02.txt")

    def test_imp_mat_parse_file(self):
        mat: Matrix = matpak.imp_mat_file("tests/test_mat_03.txt")
        self.assertListEqual(mat.raw, [
            [Decimal("1.0"), Decimal("2.0"), Decimal("3.0")],
            [Decimal("4.0"), Decimal("5.0"), Decimal("6.0")],
            [Decimal("7.0"), Decimal("8.0"), Decimal("9.0")],
            [Decimal("11.0"), Decimal("12.0"), Decimal("13.0")],
            [Decimal("14.0"), Decimal("15.0"), Decimal("16.0")],
            [Decimal("17.0"), Decimal("18.0"), Decimal("19.0")],
        ])


class TestVecIOFuncs(unittest.TestCase):
    def test_imp_vec_file_fail_on_not_existed_file(self):
        with self.assertRaises(FileNotFoundError):
            matpak.imp_vec_file("unexisted_file.txt")

    def test_imp_vec_file_empty_line(self):
        with self.assertRaises(VectorFileInvalid):
            matpak.imp_vec_file("tests/test_vec_01.txt")

    def test_imp_vec_file_contains_illegal_chars(self):
        with self.assertRaises(VectorFileInvalid):
            matpak.imp_vec_file("tests/test_vec_02.txt")

    def test_imp_vec_parse_file(self):
        vec: Vector = matpak.imp_vec_file("tests/test_vec_03.txt")
        self.assertListEqual(vec.raw, [Decimal("1.0"), Decimal("2.0"), Decimal("3.0"), Decimal("4.0"), Decimal("5.0")])


if __name__ == "__main__":
    unittest.main()
