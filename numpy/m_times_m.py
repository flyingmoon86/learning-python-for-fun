def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    # 获取矩阵a的行数和列数
    a_rows = len(a)
    a_cols = len(a[0]) if a_rows > 0 else 0
    # 获取矩阵b的行数和列数 
    b_rows = len(b)
    b_cols = len(b[0]) if b_rows > 0 else 0
    # 检查矩阵是否可以相乘
    if a_cols != b_rows:
        raise ValueError("Incompatible matrix dimensions for multiplication.")
    # 初始化结果矩阵c，大小为a的行数 x b的列数
    c = [[0 for _ in range(b_cols)] for _ in range(a_rows)]
    # 进行矩阵乘法运算
    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(a_cols):
                c[i][j] += a[i][k] * b[k][j]
    return c