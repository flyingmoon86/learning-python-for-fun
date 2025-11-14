import numpy as np

def transform_matrix(A: list[list[int | float]],
                     T: list[list[int | float]],
                     S: list[list[int | float]]) -> list[list[float]] | int:
    A = np.array(A, dtype=float)
    T = np.array(T, dtype=float)
    S = np.array(S, dtype=float)
    
    # Check invertibility of T and S
    if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
        return -1  # Non-invertible matrices
    
    try:
        T_inv = np.linalg.inv(T)
        transformed_matrix = T_inv @ A @ S
        return transformed_matrix.tolist()
    except np.linalg.LinAlgError:
        return -1  # Just in case of numerical instability or unexpected failure

# Example usage:
A = [[1, 2],
     [3, 4]]

T = [[2, 0],
     [0, 1]]

S = [[1, 1],
     [0, 1]]

print(transform_matrix(A, T, S))
