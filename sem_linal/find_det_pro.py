import cmath
import timeit

import numpy as np
from time import time
import scipy.linalg as sla


# import matplotlib.pyplot as plt
from IPython.utils.tests.test_wildcard import o


def my_det(X):
    X = np.array(X, dtype="float64")
    if X.shape[0] != X.shape[1]:
        raise ValueError()
    elif X.shape[0] == 1:
        return X[0, 0]
    else:
        vector = X[:, 0]
        swap = 2
        max_num = max(vector)
        if max_num == 0:
            return 0
        id_max = vector.argmax(axis=0)
        if id_max != 0:
            save = X[0].copy()
            X[0] = X[id_max]
            X[id_max] = save
            swap -= 1
        for i in range(1, X.shape[0]):
            multiply_koeff = X[i, 0] / X[0, 0]
            X[i] -= multiply_koeff * X[0]
        return (-1) ** swap * X[0, 0] * \
               my_det(X[np.ix_(range(1, X.shape[0]), range(1, X.shape[1]))])

#
# def my_paskal(dim):
#     P = np.ones((dim, dim))
#     for i in range(1, dim):
#         for j in range(1, dim):
#             P[i, j] = P[i - 1, j] + P[i, j - 1]
#     return P
#
#
# print(my_det(my_paskal(30)))


def f(a, b, k):
    c = a.T.dot(b)
    d = c.diagonal()
    k = min(k, b.shape[0])
    return d[:k].sum()


# print(f(
#     np.array([
#         [1, 2, 3, 4],
#         [4, 3, 2, 1],
#         [4, 0, 0, 1],
#         [2, 1, 3, 3]]),
#     np.array([
#         [2, 8, 1, 6],
#         [5, 1, 4, 2],
#         [1, 1, 2, 3],
#         [0, 1, 2, 3]]),
#     2
# ))


def six_part():
    m = n =10
    timings1 = []
    timings2 = []
    for n in range(10, 1000, 50):
        a = np.random.rand((n, n))
        b = np.random.rand((n, m))
        extended_matrix = np.append(a, b, 1)
        startt = time()



# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# print()

def shrink_rotate(x, a, coef=1., angle=0.):
    vector = x - a
    vector *= coef

def shrink_rotate_conj(x, a, coef=1., angle=0.):
    # Your code here
    new_vector = (a * coef, x * coef)
    rotated_vector = (
        new_vector[0] * cmath.cos(angle) - new_vector[1] * cmath.sin(angle),
        new_vector[0] * cmath.sin(angle) + new_vector[1] * cmath.cos(angle),
    )
    add = rotated_vector[1] - 2 * rotated_vector[1].imag * 1j
    rotated_vector = (rotated_vector[0], add)
    return rotated_vector[1]

shrink_rotate_conj(0.5 + 0.*1j, 0. + 1.*1j, coef=0.5, angle=0.)