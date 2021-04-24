from math import sqrt
import numpy as np


def solve_system(matrix_a, column_b):
    y = []
    l_matrix = create_l_matrix(matrix_a)
    for i in range(len(matrix_a)):
        buf = 0
        for a in range(i):
            print(l_matrix[i][a])
            print(y[a])
            print(buf)
            print()
            buf += l_matrix[i][a] * y[a]
        y.append((column_b[i] - buf) / l_matrix[i][i])
    return y


def create_l_matrix(matrix_a):
    l_matrix = []
    for i in range(len(matrix_a)):
        buff = []
        for a in range(len(matrix_a[i])):
            buff.append(0)
        l_matrix.append(buff)
    for k in range(len(matrix_a)):
        l_k = []
        for i in range(k):
            l_k.append(l_matrix[k][i])
        l_k_2 = [elem ** 2 for elem in l_k]
        l_matrix[k][k] = sqrt(matrix_a[k][k] - sum(l_k_2))
        for i in range(k + 1, len(l_matrix)):
            l_i = []
            for a in range(k):
                l_i.append(l_matrix[i][a])
            multiply_list = np.multiply(l_k, l_i)
            l_matrix[i][k] = (matrix_a[i][k] - sum(multiply_list)) / l_matrix[k][k]
    return l_matrix
