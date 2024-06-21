import unittest
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to be added")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to be subtracted")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrices must have appropriate dimensions to be multiplied")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __eq__(self, other):
        return self.data == other.data

# Unit Test
class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        self.matrix1 = Matrix([[1, 2], [3, 4]])
        self.matrix2 = Matrix([[5, 6], [7, 8]])
        self.sum_result = Matrix([[6, 8], [10, 12]])
        self.sub_result = Matrix([[-4, -4], [-4, -4]])
        self.mul_result = Matrix([[19, 22], [43, 50]])

    def test_addition(self):
        self.assertEqual(self.matrix1 + self.matrix2, self.sum_result)

    def test_subtraction(self):
        self.assertEqual(self.matrix1 - self.matrix2, self.sub_result)

    def test_multiplication(self):
        self.assertEqual(self.matrix1 * self.matrix2, self.mul_result)

if __name__ == '__main__':
    unittest.main()