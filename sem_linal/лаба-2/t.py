import numpy
import matplotlib
from scipy import linalg

data_train = numpy.loadtxt('./train.txt', delimiter=',')
data_test = numpy.loadtxt('./test.txt', delimiter=',')

X_train = data_train[:,0]
Y_train = data_train[:,1]

# Сделайте то же для тестовой выборки
X_test = data_test[:,0]
Y_test = data_test[:,1]

def polynom(X_data, y_data, degree):
    X_data_cpy = X_data.copy()
    y_data_cpy = y_data.copy()
    data_amount = X_data.size
    X_matrix = numpy.array([numpy.ones(data_amount)]).T
    for deg in range(1, degree + 1):
        additional_column = numpy.array([X_data_cpy]).T ** deg
        X_matrix = numpy.concatenate((X_matrix, additional_column), 1)
    pseudosolution = numpy.dot(
        numpy.dot(
            linalg.inv(
                numpy.dot(X_matrix.T.copy(), X_matrix)
            ),
            X_matrix.T.copy()
            ),
        y_data_cpy
    )
    return pseudosolution.reshape(-1)

def val_in_dot(polynom, dot):
    res = 0
    for deg, coeff in enumerate(polynom):
        res += coeff * dot ** deg
    return res
xp =  numpy.arange(-1, 1, 0.1)
polynom_21 = polynom(X_train, Y_train, 21)
y_plot_21 = [val_in_dot(polynom_21, val) for val in xp]
print()