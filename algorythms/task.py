import cmath
import numpy as np

def shrink_rotate(X, A, coef = 1., alpha = 0.):
    vector = (A, X)
    new_vector = (A * coef, X * coef)
    rotated_vector = (
            new_vector[0] * cmath.cos(alpha) - new_vector[1] * cmath.sin(alpha),
            new_vector[0] * cmath.sin(alpha) + new_vector[1] * cmath.cos(alpha),
    )
    print(vector, new_vector, rotated_vector)
    return rotated_vector[1]


def shrink_rotate_conj(x, a, coef=1., angle=0.):
    new_vector = (a * coef, x * coef)
    rotated_vector = (
        new_vector[0] * cmath.cos(angle) - new_vector[1] * cmath.sin(angle),
        new_vector[0] * cmath.sin(angle) + new_vector[1] * cmath.cos(angle),
    )
    add = rotated_vector[1] - 2 * rotated_vector[1].imag * 1j
    rotated_vector = (rotated_vector[0], add)
    print(rotated_vector)
    return rotated_vector[1]

# shrink_rotate(0 + 1j, 0.5 + 0j, 2., 6.28)
shrink_rotate_conj(0 + 1j, 0.5 + 0j, 2.,)

def f(A, B, k):
    B = B.T
    minimum = min(k, A.shape[0])
    A = A[:minimum]
    B = B[:minimum]
    multiply = A.dot(B).diagonal()
    return sum(multiply)



def nastia():
    def my_det(X):
        if X[0, 0] == 0:
            i = X[:, 0].argmax(axis=0)
            for j in range(3):
                X[0,j] += X[i,j]
        i = np.flatnonzero(X[:, 0])[0]
        while X[i,0] != 0:
            for j in range(1, 3):
                y = X[i,j]
                X[i,j] *=X[0, j]
                X[0, j] = y *X[0, j]
                X[i, j] -= X[0, j]
            i = np.flatnonzero(X[:, 0])[0]

    my_det(np.array([
    [8, 4, 1],
    [1, 2, 5],
    [1, 6, 3]
]))

nastia()