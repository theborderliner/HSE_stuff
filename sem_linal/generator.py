import random

'''
    Идея такая:
        1. Раскладываем определитель на n множителей, где n - заданный порядок матрицы.
        2. Полученное разложение это числа на главной диагонали верхнетреугольной матрицы.
        3. Составляем верхнетругольную матрицу, на главной диагонали которой наше разложение, а 
            выше неё - случайные целые числа (можно и не целые, но я хочу целые)
        4. К полученной верхнетреугольной матрице начинаем применять рандомные элементарные преобразования 
            не помню какого типа, короче того, который не меняет определитель
        5. Вроде всё, получили то, что требовалось.
'''


def is_prime(num, start):  # проверяет число на простоту, сложность: O(sqrt(n)).
    div = start  # пока start нужен, чтобы функция разложила число на <= n множителей, где n - порядок матрицы.
    while div ** 2 <= num and num % div != 0:
        div += 1

    return div ** 2 > num, div  # возвращаем булевый ответ проверки на  простоту, ну и заодно
    # найденый делитель числа, чтобы дважды не вставать.


def construct_triangle_matrix(size, diagonal):  # собираем врхнетругольный вид
    matrix = []
    for i in range(size):  # вот вы знали, что вот такая конструкция: matrix = [[0] * n] * n,
        matrix.append([0] * size)  # создаст квадратный массив n на n, В котором при измении
        # одной строки будут меняться сразу все? Я вот не знал...

    random_pain = 1  # регулятор боли - генерируемых чисел в матрице

    for i in range(size):
        for j in range(size):
            if j == i:
                matrix[i][j] = diagonal[i]
            elif i < j:
                matrix[i][j] = random.randint(0, 10 ** random_pain - 1)  # -1 чтобы число было меньше последнего десятка

    return matrix


def random_transformations(matrix):  # случайные элементарные преобразования
    size = len(matrix)
    random_pain = 1  # аналогично
    '''
         На самом деле не очень случайные, мы будем брать последний столбец матрицы (потому что он 
         почти полностью сгенерирован), умножать его на случайное число и прибавлять к предыдущему,
         потом то же самое сделаем с ним и тем, который до него и т.д.
    '''

    for i in range(size - 1, 0, -1):
        random_multyplier = random.randint(1, 10 ** random_pain - 1)
        for j in range(size):
            matrix[j][i - 1] += matrix[j][i] * random_multyplier

    return matrix


def generate_matrix(size, determinant):
    det_dividers = [1] * size
    while not is_prime(determinant, size)[0]:  # будем делить определитель пока он не станет простым
        div = is_prime(determinant, size)[1]
        determinant //= div
        det_dividers.append(div)
    det_dividers.append(determinant)
    det_dividers = det_dividers[len(det_dividers) - size:]  # в массиве элементов больше, чем size,
    # все лишние отрежем, останется только наши делители и несколько единиц

    matrix = construct_triangle_matrix(size, det_dividers)
    matrix = random_transformations(matrix)  # всё, на этом этапе уже готовая матрица

    return matrix  # в соседнем файле находится функция, которая находит определитель, можно проверить
