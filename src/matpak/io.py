import re
from decimal import Decimal

from .types import lst_dec_1d_t, lst_dec_2d_t
from .errors import MatrixFileInvalid, VectorFileInvalid
from .mat import Matrix
from .vec import Vector


def imp_mat_file(file: str, sep: str = ',') -> Matrix:
    """
    Import matrix from a file. The file containing matrix should have the following syntax:

        a11,a12,a13\n
        a21,a22,a23\n
        a31,a32,a33

    rules:
        - each file contains only one matrix.
        - each line represents a row in matrix.
        - no empty lines between matrix rows allowed.
        - seperator char should be same for all elements.
        - no spaces allowed.
        - for negative elements, character '-' is used before element. for positive elements, it is not required to write down '+' char.
        - last char in end of each line (except for last line) should be same for all lines.
        - last line could also be newline.
        - rows count and cols count is gathered from file automatically.
        - cols count in each row should be same as other rows.
        - elements would be read as Decimal floating-point numbers with precision that is defined in configurations.

    return value is a class of type Matrix.

    if there is any issue, an exception would be raised. beside standard exceptions, there are following
    custom exceptions that would be raised in special scenarios:
        1- file empty or no matrix exists: MatrixFileInvalid

    :param file: path to matrix file. each line in file represents a
    :param sep: file's elements separator char; by default, it is comma ','.

    :return: Matrix
    """
    with open(file) as mat_f:
        ls = mat_f.readlines()

        if len(ls) <= 0:
            raise MatrixFileInvalid(file, "does not contain any matrix")

        ls = list(map(lambda l: l.strip(), ls))

        # delete any blank lines
        ls = list(filter(lambda l: l.strip() != '', ls))

        # in matrix files, only 'separator char', 0-9 and '.' are allowed. so filtering other chars
        if re.search(f"[^0-9.{sep}]", ''.join(ls)):
            raise MatrixFileInvalid(file,
                                    f"contains non-standard chars. it must only contain chars: ['{sep}','0','1','2','3','4','5','6','7','8','9','.'] and standard newline char")

        # ignore first empty lines in file by increasing 'base pointer' var until first non-empty line is reached.
        bp = 0
        while bp < len(ls) and len(ls[bp].strip()) == 0:
            bp += 1

        if bp >= len(ls):
            raise MatrixFileInvalid(file, "does not contain any matrix")

        mat: lst_dec_2d_t = list(map(lambda l: list(map(lambda el: Decimal(el.strip()), l.split(sep))), ls))
        del ls

        # rows should be at least 1, there is no need to check
        rows_cnt = len(mat)
        cols_cnt = len(mat[0])

        return Matrix(rows_cnt, cols_cnt, mat)


def imp_vec_file(file: str) -> Vector:
    """
    Import vector from a file. The file containing vector should have the following syntax:

        a1\n
        a2\n
        a3

    rules:
        - each file contains only one vector.
        - each line represents a row in vector.
        - no spaces allowed.
        - for negative elements, character '-' is used before element. for positive elements, it is not required to write down '+' char.
        - last char in end of each line (except for last line) should be same for all lines.
        - last line could also be newline.
        - rows count of vector is gathered from file automatically.
        - elements would be read as Decimal floating-point numbers with precision that is defined in configurations.

    :param file: path to vector file. each element in file represents a vector element.

    :return: vec_t
    """
    with open(file) as vec_f:
        ls = vec_f.readlines()

        if len(ls) <= 0:
            raise VectorFileInvalid(file, "does not contain any matrix")

        # delete any blank lines
        ls = list(map(lambda l: l.strip(), ls))
        ls = list(filter(lambda l: l.strip() != '', ls))

        # in vector files, only 0-9 and '.' are allowed. so filtering other chars
        if re.search(f"[^0-9.]", ''.join(ls)):
            raise VectorFileInvalid(file,
                                    f"contains non-standard chars. it must only contain chars: ['0','1','2','3','4','5','6','7','8','9','.'] and standard newline char")

        # ignore first empty lines in file by increasing 'base pointer' var until first non-empty line is reached.
        bp = 0
        while bp < len(ls) and len(ls[bp].strip()) == 0:
            bp += 1

        if bp >= len(ls):
            raise VectorFileInvalid(file, "does not contain any vector")

        vec: lst_dec_1d_t = list(map(lambda el: Decimal(el.strip()), ls))
        del ls

        # rows should be at least 1, there is no need to check
        rows_cnt = len(vec)

        return Vector(rows_cnt, vec)
