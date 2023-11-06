# Класс Matrix (обработка матриц)
class Matrix:
    def __init__(self, array: list):
        self.array = array

    def __add__(self, other):
        if len(self.array) == len(other.array) and len(self.array[0]) == len(other.array[0]):
            array = [[self.array[i][j] + other.array[i][j] for j in range(len(self.array[0]))]
                     for i in range(len(self.array))]
            return Matrix(array)
        else:
            return "Матрицы различных размерностей"

    def __sub__(self, other):
        # print(self.array, other.array, sep='\n')
        if len(self.array) == len(other.array) and len(self.array[0]) == len(other.array[0]):
            array = [[self.array[i][j] - other.array[i][j] for j in range(len(self.array[0]))]
                     for i in range(len(self.array))]
            return Matrix(array)
        else:
            return "Матрицы различных размерностей"

    def __mul__(self, other):
        array = [[self.array[i][j] * other for j in range(len(self.array[0]))]
                 for i in range(len(self.array))]
        return Matrix(array)

    def transposition(self):
        array = [[self.array[j][i] for j in range(len(self.array))] for i in range(len(self.array[0]))]
        return Matrix(array)

    @classmethod
    def identity_matrix(cls, m: int, n: int):
        array = [[1 for _ in range(n)] for _ in range(m)]
        return cls(array)

    @classmethod
    def zero_matrix(cls, m: int, n: int):
        array = [[0 for _ in range(n)] for _ in range(m)]
        return cls(array)

    @classmethod
    def diagonal_matrix(cls, array_in: list):
        array = [[array_in[i][j] if i == j else 0 for j in range(len(array_in[0]))] for i in range(len(array_in))]
        return cls(array)

    def dimension_matrix(self):
        return len(self.array), len(self.array[0])

    def number_of_elements(self):
        return len(self.array) * len(self.array[0])

    def sum_of_elements(self):
        return sum([sum(i) for i in self.array])

    def negative_to_zero(self):
        array = [[0 if self.array[i][j] < 0 else self.array[i][j] for j in range(len(self.array[0]))]
                 for i in range(len(self.array))]
        return Matrix(array)

    def __eq__(self, other):
        out = False
        if len(self.array) == len(other.array) and len(self.array[0]) == len(other.array[0]):
            for i in range(len(self.array)):
                for j in range(len(self.array[i])):
                    if self.array[i][j] != other.array[i][j]:
                        return out
            out = True
        return out

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
array_5 = [[1, 3, -2], [9, 4, 2], [2, -4, -2]]
array_6 = array_5
array_7 = array_4

array_1 = Matrix(array_1)
array_2 = Matrix(array_2)
array_3 = Matrix(array_3)
array_4 = Matrix(array_4)
array_5 = Matrix(array_5)

res = array_1 + array_2
print(res)
res = array_3 + array_2
print(res)
res = array_3 + array_5
print(res)

res = array_1 - array_2
print(res)
res = array_3 - array_2
print(res)
res = array_3 - array_5
print(res)

print(array_1)

res = array_1 * 2
print(res)

print(array_2.transposition())
print(array_1.transposition())

print(array_2.negative_to_zero())
print(array_5.negative_to_zero())

print(array_1.dimension_matrix())
print(array_4.dimension_matrix())

print(array_1.number_of_elements())
print(array_4.number_of_elements())

print(array_1.sum_of_elements())
print(array_5.sum_of_elements())

print(array_1 == array_3)
print(array_2 == array_3)
print(array_5 == array_3)

print(Matrix.identity_matrix(2, 3))
print(Matrix.identity_matrix(5, 3))

print(Matrix.zero_matrix(2, 3))
print(Matrix.zero_matrix(5, 3))
print(Matrix.zero_matrix(4, 4))

print(Matrix.diagonal_matrix(array_6))
print(Matrix.diagonal_matrix(array_7))

print('----------------')
print()
