from __future__ import annotations
from decimal import Decimal

from .errors import VectorDimensionInvalid, MultiplicationDimensionMismatched
from .types import lst_dec_1d_t


class Vector:
    def __init__(self, rows: int, init_vec: lst_dec_1d_t | None = None):
        """
        initialize a rows count vector and init_vec list

        :param rows: vector rows count.
        :param init_vec: initial values for vector; or None as default for zero vector.
        """
        if rows <= 0:
            raise VectorDimensionInvalid(f"vector with {rows} rows is invalid.")

        self.__rows = rows

        if init_vec is None:
            self.__raw_vec: lst_dec_1d_t = [Decimal(0.0)] * rows
        else:
            self.__raw_vec: lst_dec_1d_t = init_vec

    @property
    def shape(self) -> tuple[int, int]:
        """
        get vector rows.

        :return: a tuple of vector rows*1
        """
        return self.__rows, 1

    @property
    def raw(self) -> lst_dec_1d_t:
        """
        get raw vector 1D list of Decimal values.

        :return: lst_dec_1d_t
        """
        return self.__raw_vec

    def set(self, row: int, val: Decimal):
        """
        store 'val' in vector[row] address.

        :param row: number of row.
        :param val: value to be stored inside vector[row] address.
        """

        if row > self.__rows or row < 0:
            raise ValueError(f"address {row} is not in boundaries of vector with {self.__rows} rows")

        self.__raw_vec[row] = val

    def get(self, row: int) -> Decimal:
        """
        get value of vector[row] address.

        :param row: number of row.
        :return: Decimal
        """

        if row > self.__rows:
            raise ValueError(f"address {row} is not in boundaries of vector with {self.__rows} rows")

        return self.__raw_vec[row]

    # multiplication methods

    def multiply(self, rhs: "Matrix") -> "Matrix":
        from .mat import Matrix
        """
        multiply row-major(col-major and row-major are not different in vector-matrix multiplication) one vector and other matrix or vecto.

        :param rhs: right hand side, should be Matrix 1*m.
        :return: Matrix
        """

        self_shape = self.shape

        if self_shape[1] != rhs.shape[0]:
            raise MultiplicationDimensionMismatched(self_shape, rhs.shape)

        res: Matrix = Matrix(self_shape[0], rhs.shape[1])

        for i in range(self_shape[0]):
            for k in range(rhs.shape[1]):
                tmp = res.get(i, k)
                tmp += self.get(i) * rhs.get(0, k)
                res.set(i, k, tmp)

        return res