import cmath

def shrink_rotate(X, A, coef = 1., alpha = 0.):
    vector = (A, X)
    new_vector = (A * coef, X * coef)
    rotated_vector = (
            new_vector[0] * cmath.cos(alpha) - new_vector[1] * cmath.sin(alpha),
            new_vector[0] * cmath.sin(alpha) + new_vector[1] * cmath.cos(alpha),
    )
    print(vector, new_vector, rotated_vector)

shrink_rotate(0 + 1j, 0.5 + 0j, 2., 6.28)
