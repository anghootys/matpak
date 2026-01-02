from decimal import Decimal

from .errors import MatrixDimensionInvalid
from .types import lst_dec_2d_t


class Matrix:
    def __init__(self, rows: int, cols: int, init_mat: lst_dec_2d_t | None = None):
        """
        initialize rows*cols matrix with init_mat 2D list elements.

        :param rows: matrix rows count.
        :param cols: matrix cols count.
        :param init_mat: initial rows*cols 2D Decimal values for matrix elements; or None as default for zero matrix.
        """

        if rows <= 0 or cols <= 0:
            raise MatrixDimensionInvalid(f"matrix {rows}x{cols} rows count or cols count are invalid.")

        self.__rows = rows
        self.__cols = cols

        if init_mat is None:
            self.__raw_mat: lst_dec_2d_t = [[Decimal(0.0)] * cols for _ in range(rows)]
        else:
            for i in range(rows):
                if len(init_mat[i]) != cols:
                    raise MatrixDimensionInvalid(
                        f"matrix cols count should be {cols} but found a row with cols count of {len(init_mat[i])}")
            self.__raw_mat: lst_dec_2d_t = init_mat

    @property
    def shape(self) -> tuple[int, int]:
        """
        get matrix dimensions.

        :return: a tuple of matrix rows*cols
        """
        return self.__rows, self.__cols

    @property
    def raw(self) -> lst_dec_2d_t:
        """
        get raw matrix 2D list of Decimal values.

        :return: lst_dec_2d_t
        """
        return self.__raw_mat

    def set(self, row: int, col: int, val: Decimal):
        """
        store 'val' in matrix[row][col] address.

        :param row: number of row.
        :param col: number of col.
        :param val: value to be stored inside matrix[row][col] address.
        """

        if row > self.__rows or col > self.__cols or row < 0 or col < 0:
            raise ValueError(f"address {row}*{col} is not in boundaries of matrix {self.__rows}*{self.__cols}")

        self.__raw_mat[row][col] = val

    def get(self, row: int, col: int) -> Decimal:
        """
        get value of matrix[row][col] address.

        :param row: number of row.
        :param col: number of col.
        :return: Decimal
        """

        if row > self.__rows or col > self.__cols:
            raise ValueError(f"address {row}*{col} is not in boundaries of matrix {self.__rows}*{self.__cols}")

        return self.__raw_mat[row][col]
