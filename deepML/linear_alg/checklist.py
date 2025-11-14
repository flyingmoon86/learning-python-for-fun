import numpy as np

# 1. shape 和变形
a = np.zeros((2, 3, 4))
b = a.reshape(6, 4)
c = b[:, None, :]      # 插入一维
d = c.squeeze()        # 删除维度

# 2. 索引
x = a[0]               # 切片
y = a[:, 1:3]
z = a[a > 0.5]         # 布尔索引

# 3. 广播
p = np.ones((3, 1))
q = np.ones((1, 4))
pq = p + q             # (3, 4)

# 4. 常见数学操作
np.sum(a, axis=0)
np.mean(a, axis=1)
np.max(a, axis=-1)

# 5. 矩阵运算
M = np.random.randn(32, 64)
W = np.random.randn(64, 10)
out = M @ W            # (32, 10)

# 6. 拼接与转置
np.concatenate([M, M], axis=0)
np.transpose(a, (2, 1, 0))
