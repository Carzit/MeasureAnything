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

#相机内参矩阵求逆
matrix = np.array([[618960/1500, 0, 853],
                   [0, 628960/1500, 640],
                   [0, 0, 1]])
inverse = np.linalg.inv(matrix)

#坐标变换
def transformation(f):
    x = np.matmul(inverse, f)
    return x

# 示例输入
'''
f11 = np.array([1232, 855, 167])
f21 = np.array([1313, 816, 171])
f31 = np.array([1332, 619, 171])
f41 = np.array([-81+1542, -39+969, 175])
f1 = transformation(f11)
f2 = transformation(f21)
f3 = transformation(f31)
f4 = transformation(f41)
result = calculate_formula(f1, f2, f3, f4)
print(result)

>>1.8034015103529788
  0.46512585569543696
  0.6178852883037119
'''