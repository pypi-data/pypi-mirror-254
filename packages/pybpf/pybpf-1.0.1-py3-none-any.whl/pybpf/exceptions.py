class EmptyFileException(Exception):
    def __init__(self, message="The E57 file is empty") -> None:
        super().__init__(message)


class UnknownDataTypeException(Exception):
    def __init__(self, message="Unknown data BPF data type") -> None:
        super().__init__(message)
