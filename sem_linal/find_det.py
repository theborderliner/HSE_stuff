X = 0

the_matrix = [[601, 75, 10, 5], [368, 46, 6, 2], [728, 91, 13, 9], [280, 35, 5, 5]]
the_order = 4
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
    drawMatrix(matrix)
    determinant = 1

    for i in range(len(matrix)):
        determinant *= matrix[i][i]

    return (-1) ** sign * determinant


print("Определитель равен: ", getDeterminant(the_matrix, the_order))
print(iters)
