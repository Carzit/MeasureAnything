import numpy as np


def calculate_formula(f1, f2, f3, f4):
    # 计算 C12 和 C13
    C12 = calculate_C12(f1, f2, f3, f4)
    C13 = calculate_C13(f1, f2, f3, f4)

    # 分子
    numerator = np.dot(C12 * f2 - f1, C12 * f2 - f1)

    # 分母
    denominator = np.dot(C13 * f3 - C12 * f2, C13 * f3 - C12 * f2)

    # 线段比例
    result = np.sqrt(numerator / denominator)
    return result

def calculate_C12(f1, f2, f3, f4):
    matrix1 = np.array([f3, f4, f1])
    det1 = np.linalg.det(matrix1)
    matrix2 = np.array([f2, f3, f4])
    det2 = np.linalg.det(matrix2)
    C12 = det1 / det2
    print(C12)
    return C12

def calculate_C13(f1, f2, f3, f4):
    matrix1 = np.array([f4, f1, f2])
    det1 = np.linalg.det(matrix1)
    matrix2 = np.array([f2, f3, f4])
    det2 = np.linalg.det(matrix2)
    C13 = det1 / det2
    print(C13)
    return C13

# 示例输入
f1 = np.array([379, 215, 167])
f2 = np.array([460, 176, 163])
f3 = np.array([479, -21, 171])
f4 = np.array([398, -60, 175])
result = calculate_formula(f1, f2, f3, f4)

print(result)