# Q. Write an algorithm such that if an element in an MxN matrix is 0, its
# entire row and column are set to 0.
# Time complexity: O(NxM)
# Space complexity: O(N + M)

import unittest


def zero_matrix(matrix):
    zero_rows = []  # Rows with zero in it
    zero_columns = []  # Columns with zero in it

    # Traverse matrix
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == 0:
                zero_rows.append(i)
                zero_columns.append(j)

    for i, row in enumerate(matrix):
        for j in range(len(row)):
            if i in zero_rows or j in zero_columns:
                matrix[i][j] = 0


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
