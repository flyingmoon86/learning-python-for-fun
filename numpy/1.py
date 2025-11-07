import numpy as np

A = np.array([[1,2],[3,4]])
b = np.array([5,6])

x = np.linalg.solve(A, b)   # 求解 Ax=b
print(A) 
print(b)
print(x)  # 输出解 x