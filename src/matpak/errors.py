class MatrixFileInvalid(Exception):
    def __init__(self, file: str, msg: str):
        super().__init__(f"matrix file '{file}' {msg}")

class MatrixDimensionInvalid(Exception):
    pass

class VectorFileInvalid(Exception):
    def __init__(self, file: str, msg: str):
        super().__init__(f"vector file '{file}' {msg}")

class VectorDimensionInvalid(Exception):
    pass

class MultiplicationDimensionMismatched(Exception):
    def __init__(self, lhs_shape: tuple[int, int], rhs_shape: tuple[int, int]):
        super().__init__(f"could not multiply {lhs_shape[0]}x{lhs_shape[1]} shaped matrix by {rhs_shape[0]}x{rhs_shape[1]} shaped one")