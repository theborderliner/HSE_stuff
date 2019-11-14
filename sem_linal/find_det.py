X = -6

the_matrix = [
    [0, 0, 0, 9, X, 0],
    [0, 0, 5, 9, X, X],
    [5, 0, 0, 9, 8, 9],
    [0, 2, 0, 0, 4, 7],
    [X, 0, 0, X, 0, X],
    [0, 4, 5, 8, 5, 8],
]
the_order = 6
iters = 0


def setTriangleMode(matrix, order):
    sign_switch = 0
    current_line = 0
    global iters
    while (current_line != order - 1):
        for i in range(current_line + 1, order):
            line_shift = 1

            while matrix[current_line][current_line] == 0:

                if line_shift >= order - 1:
                    return [[0]], 0

                matrix[current_line], matrix[current_line + line_shift] = matrix[current_line + line_shift], matrix[
                    current_line]
                line_shift += 1
                sign_switch += 1

            multiply_koeff = matrix[i][current_line] / matrix[current_line][current_line]

            for j in range(order):
                matrix[i][j] -= matrix[current_line][j] * multiply_koeff

            iters += 1

        current_line += 1

    return matrix, sign_switch


def drawMatrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()
    print()


def getDeterminant(matrix, order):
    matrix, sign = setTriangleMode(matrix, order)
    # drawMatrix(matrix)
    determinant = 1

    for i in range(len(matrix)):
        determinant *= matrix[i][i]

    return round((-1) ** sign * determinant)


print("Определитель равен: ", getDeterminant(the_matrix, the_order))
# print(iters)
