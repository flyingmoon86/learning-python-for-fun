import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # 将列表转换为 NumPy 数组
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float).reshape(-1, 1)  # 确保 y 是列向量

    # 正规方程计算 theta
    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    # 将 theta 转为列表并四舍五入到 1 位小数
    theta_list = [round(val[0], 1) for val in theta]

    return theta_list
