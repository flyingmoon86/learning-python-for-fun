import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

    """
    计算给定特征集合的协方差矩阵。
    
    参数:
        vectors: list[list[float]]
            每个内层列表表示一个特征（feature），包含该特征的所有观测值。
            例如：
            [
                [1, 2, 3],   # 特征1的观测值
                [4, 5, 6]    # 特征2的观测值
            ]
    
    返回:
        协方差矩阵（list[list[float]]）
    """
    # 转为 NumPy 数组，行表示特征，列表示观测
    data = np.array(vectors, dtype=float)
    
    # np.cov 默认每一行是一个变量（特征），列是样本
    cov_matrix = np.cov(data, bias=False)  # bias=False 表示除以 (N-1)
    
    # 转为普通 Python 列表返回
    return cov_matrix.tolist()
