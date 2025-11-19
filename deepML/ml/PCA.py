import numpy as np 

def pca(data: np.ndarray, k: int) -> np.ndarray:
    # Step 1: Standardize
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0, ddof=1)
    X = (data - mean) / std

    # Step 2: Covariance Matrix
    cov_matrix = np.cov(X, rowvar=False)

    # Step 3: Eigen Decomposition
    eig_vals, eig_vecs = np.linalg.eigh(cov_matrix)

    # Step 4: Sort by eigenvalues (descending)
    idx = np.argsort(eig_vals)[::-1]
    eig_vecs = eig_vecs[:, idx]

    principal_components = eig_vecs[:, :k]

    # Step 5: Fix sign (make first non-zero element positive)
    for i in range(principal_components.shape[1]):
        col = principal_components[:, i]
        for v in col:
            if abs(v) > 1e-8:
                if v < 0:
                    principal_components[:, i] *= -1
                break
    
    return np.round(principal_components, 4)
