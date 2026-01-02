from .io import imp_mat_file, imp_vec_file
from .errors import *

from .mat import Matrix
from .vec import Vector

from .types import *

__all__ = [
    # utility funcs
    "imp_mat_file", "imp_vec_file",

    # classes
    "Matrix", "Vector",

    # types
    "lst_dec_1d_t", "lst_dec_2d_t",

    # error types
    "MatrixFileInvalid", "MatrixDimensionInvalid",
    "VectorFileInvalid", "VectorDimensionInvalid"
]
