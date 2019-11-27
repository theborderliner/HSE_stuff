import numpy as np
import scipy.linalg as sla
# import matplotlib.pyplot as plt


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

def my_paskal(dim):
    P = np.ones((dim, dim))
    for i in range(1, dim):
        for j in range(1, dim):
            P[i, j] = P[i - 1, j] + P[i, j - 1]
    return P

print(my_det(my_paskal(30)))


def f(A, B, k):
    up_border = min(A.shape[0], k)
    B = B.T
    real_A = A[:, :up_border]
    real_B = B[:up_border, :]
    print(real_A)
    print()
    print(real_B)
    print()
    print(np.multiply(A, B))


