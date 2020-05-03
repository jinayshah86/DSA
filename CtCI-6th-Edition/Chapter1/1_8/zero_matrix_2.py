# Q. Write an algorithm such that if an element in an MxN matrix is 0, its
# entire row and column are set to 0.
# Time complexity: O(NxM)
# Space complexity: O(1)

import unittest


def nullfiy_row(matrix, row_index):
    for col_index in range(len(matrix[row_index])):
        matrix[row_index][col_index] = 0


def nullfiy_col(matrix, col_index):
    for row in matrix:
        row[col_index] = 0


def zero_matrix(matrix):
    first_row_zero = False
    first_col_zero = False

    # Check for zero in first row
    for cell in matrix[0]:
        if cell == 0:
            first_row_zero = True
            break

    # Check for zero in first column
    for row in matrix:
        if row[0] == 0:
            first_col_zero = True
            break

    # Mark row and column headers as 0 for cell with 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Nullify columns based on values of first row
    for col_index in range(1, len(matrix[0])):
        if matrix[0][col_index] == 0:
            nullfiy_col(matrix, col_index)

    # Nullify rows based on values of first column
    for row_index in range(1, len(matrix)):
        if matrix[row_index][0] == 0:
            nullfiy_row(matrix, row_index)

    # Nullify first row and column as necessary
    if first_row_zero:
        nullfiy_row(matrix, 0)
    if first_col_zero:
        nullfiy_col(matrix, 0)


class TestZeroMatrix(unittest.TestCase):
    def test_2x2(self):
        original_matrix = [
            [0, 1],
            [1, 1],
        ]
        expected_matrix = [[0, 0], [0, 1]]
        zero_matrix(original_matrix)
        self.assertEqual(expected_matrix, original_matrix)

    def test_3x2(self):
        original_matrix = [
            [0, 1],
            [1, 1],
            [1, 1],
        ]
        expected_matrix = [
            [0, 0],
            [0, 1],
            [0, 1],
        ]
        zero_matrix(original_matrix)
        self.assertEqual(expected_matrix, original_matrix)

    def test_3x4(self):
        original_matrix = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 0],
        ]
        expected_matrix = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ]
        zero_matrix(original_matrix)
        self.assertEqual(expected_matrix, original_matrix)


if __name__ == "__main__":
    unittest.main()
