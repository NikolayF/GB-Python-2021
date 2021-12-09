import random as ran

class Matrix:

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix_list = []
        for row in range(self.num_rows):
            self.matrix_list.append([0] * self.num_cols)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.matrix_list[row][col] = ran.randint(1, 9)

    def __str__(self):
        return_str = ''
        for row in self.matrix_list:
            for elem in row:
                return_str += str(elem) + ' '
            return_str += '\n'
        return return_str

    def __add__(self, other):
        result = self.matrix_list
        for i in range(len(self.matrix_list)):

            for j in range(len(self.matrix_list[0])):
                result[i][j] = self.matrix_list[i][j] + other.matrix_list[i][j]

        for r in result:
            print(r)


matrix_1 = Matrix(3, 3)
matrix_2 = Matrix(3, 3)

print(matrix_1)
print(matrix_2)

matrix_1 + matrix_2
