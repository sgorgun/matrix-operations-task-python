"""Templates for programming assignments: basic matrix operations."""

from typing import List


def transpose(matrix: List[List[float]]) -> List[List[float]]:
    """Returns a view of a given matrix with axes transposed.

    Args:
        matrix: List[List[float]], a given numeric matrix.

    Returns:
        The transposed matrix.
    """
    result = []
    for col_index in range(len(matrix[0])):
        row = []
        for row_index in range(len(matrix)):
            row.append(matrix[row_index][col_index])
        result.append(row)

    return result


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
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices are not compatible")

    result = []
    for row_index in range(len(matrix_a)):
        row = []
        for col_index in range(len(matrix_a[0])):
            row.append(matrix_a[row_index][col_index] + matrix_b[row_index][col_index])
        result.append(row)

    return result


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
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Matrices are not compatible for multiplication.")
    
    result = []
    for row_index in range(len(matrix_a)):
        row = []
        for col_index in range(len(matrix_b[0])):
            element = 0
            for k in range(len(matrix_a[0])):
                element += matrix_a[row_index][k] * matrix_b[k][col_index]
            row.append(element)
        result.append(row)

    return result
