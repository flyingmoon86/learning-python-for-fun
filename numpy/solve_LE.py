import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    """
    Solve the system of linear equations Ax = b using the Jacobi iterative method.

    Parameters:
    A (np.ndarray): Coefficient matrix.
    b (np.ndarray): Ordinate matrix.
    n (int): Number of iterations.

    Returns:
    list: Approximate solution vector x after n iterations.
    """
    # Initialize the solution vector with zeros
    x = np.zeros_like(b, dtype=np.float64)

    # Perform n iterations of the Jacobi method
    for _ in range(n):
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            s = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - s) / A[i, i]
        x = x_new
    return x