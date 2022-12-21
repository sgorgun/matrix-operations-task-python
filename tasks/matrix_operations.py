"""Templates for programming assignments: basic matrix operations."""

from typing import List


def transpose(matrix: List[List[float]]) -> List[List[float]]:
    """Returns a view of a given matrix with axes transposed.

    Args:
        matrix: List[List[float]], a given numeric matrix.

    Returns:
        The transposed matrix.
    """
    pass


def add_matrices(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
    """Returns a sum of two given matrices.

    Args:
        matrix_a: List[List[float]], the first numeric matrix.
        matrix_b: List[List[float]], the second numeric matrix.

    Returns:
        The sum of two given matrices.

    Raises:
        ValueError: if the matrices are not compatible (dimensions differ in size).
    """
    pass


def multiply_matrices(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
    """Returns the product (result of multiplication) of two given matrices.

    Args:
        matrix_a: List[List[float]], the first numeric matrix.
        matrix_b: List[List[float]], the second numeric matrix.

    Returns:
        The product of two given matrices.

    Raises:
        ValueError: if the matrices are not compatible.
    """
    pass
