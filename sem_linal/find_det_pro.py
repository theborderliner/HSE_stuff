import numpy as np
import scipy.linalg as sla
import matplotlib.pyplot as plt


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
            X[0] = X[id_max];
            X[id_max] = save
            swap -= 1
        for i in range(1, X.shape[0]):
            multiply_koeff = X[i, 0] / X[0, 0]
            X[i] -= multiply_koeff * X[0]
        return (-1) ** swap * X[0, 0] * \
               my_det(X[np.ix_(range(1, X.shape[0]), range(1, X.shape[1]))])


# print(X)
# print(my_det(X), sla.det(X))

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


mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
                ])
v = np.array([2, 4, 6])
# print(mat * v.T)

print(f(np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
                ]), np.array([[5, 2, 1],
                              [6, 5, 5],
                              [3, 1, 1]
                              ]), 2))
