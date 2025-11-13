import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	
	X = np.array(X)
	y = np.array(y).reshape(-1, 1)
	# 添加截距项（bias term）
X_b = np.c_[np.ones((X.shape[0], 1)), X]
    # 正规方程计算参数 theta
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    return theta_best.flatten().tolist()