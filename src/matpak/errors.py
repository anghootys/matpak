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