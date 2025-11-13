def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    # Check if the input is a 2x2 matrix
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")
    a, b = matrix[0]
    c, d = matrix[1]
    determinant = a * d - b * c
    # Return 'None' if the matrix is not invertible.
    if determinant == 0:
        return None
    inverse = [[d / determinant, -b / determinant],
               [-c / determinant, a / determinant]]
    return inverse