def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'row':
        means = [sum(row) / len(row) for row in matrix]
    elif mode == 'column':
        means = [sum(col) / len(col) for col in zip(*matrix)]
    else:
        means = []
    return means


# 测试
print(calculate_matrix_mean([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]], 'column'))
# 输出: [4.0, 5.0, 6.0]
