# Класс Matrix (обработка матриц)
class Matrix:
    def __init__(self, array: list):
        self.array = array

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def transposition(self):
        pass

    def identity_matrix(self):
        pass

    def zero_matrix(self):
        pass

    def diagonal_matrix(self):
        pass

    def dimension_matrix(self):
        pass

    def number_of_elements_in_matrix(self):
        pass

    def sum_of_matrix_elements(self):
        pass

    def negative_to_zero(self):
        pass

    def equality_of_two_matrices(self):
        pass

    def __str__(self):
        out = ''
        for row in self.array:
            for i in row:
                out += str(i) + ' '
            out += '\n'
        return f"Матрица из {len(self.array)} строк(и) по {len(self.array[0])} элементов(а)\n" + out


array_1 = [[-1, 3], [0, 1], [-2, 2]]
array_2 = [[-1, 3, 4], [0, 1, 6], [-2, 2, 8]]
array_3 = [[-1, 3, 4], [0, 1, 6], [-2, 2, 8]]
array_4 = [[-1, 3, 4, 5], [0, 1, 6, -6], [-2, 2, 8, -7], [0, 1, 2, 3]]

array_1 = Matrix(array_1)
array_2 = Matrix(array_2)
array_3 = Matrix(array_3)
array_4 = Matrix(array_4)

print(array_1)
print('----------------')
print()
