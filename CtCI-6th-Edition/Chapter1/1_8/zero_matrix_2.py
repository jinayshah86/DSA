# Q. Write an algorithm such that if an element in an MxN matrix is 0, its
# entire row and column are set to 0.
# Time complexity: O(NxM)
# Space complexity: O(1)

import unittest


def zero_matrix(matrix):
    first_col_zero = False

    # Mark row and column headers as 0 for cell with 0
    for i in range(len(matrix)):
        first_col_zero = matrix[i][0] == 0 or first_col_zero
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(len(matrix) - 1, -1, -1):
        for j in range(len(matrix[i]) - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        matrix[i][0] = 0 if first_col_zero else matrix[i][0]


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
