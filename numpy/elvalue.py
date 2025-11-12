import math

def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    # 检查输入是否为 2x2
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")

    a, b = matrix[0]
    c, d = matrix[1]

    # 计算迹和行列式
    trace = a + d
    determinant = a * d - b * c

    # 计算判别式
    discriminant = trace**2 - 4 * determinant

    # 防止负判别式导致 math.sqrt 报错
    if discriminant < 0:
        return []  # 如果为复数情况，这里简单返回空列表（也可改为 complex 支持）

    sqrt_disc = math.sqrt(discriminant)

    # 计算两个特征值
    λ1 = (trace + sqrt_disc) / 2
    λ2 = (trace - sqrt_disc) / 2

    # 从大到小排序
    eigenvalues = sorted([λ1, λ2], reverse=True)

    return eigenvalues
