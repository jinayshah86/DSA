# Q. Given an image represented by an NxN matrix, where each pixel in the
# image is 4 bytes, writes a method ot rotate the image by 90 degrees. Can
# you do this in place?
# Time complexity: O(N^2); N is the size of the NxN matrix.
# Space complexity: O(N^2); N is the size of the NxN matrix.

import unittest


def rotate_90_matrix(matrix):
    size = len(matrix)
    if size == 1:   # Identity case
        return
    rotated_matrix = [[None for _ in range(size)] for _ in range(size)]
    for i, row in enumerate(matrix):
        assert len(row) == size  # Validation
        for j, cell in enumerate(row):
            rotated_matrix[i][j] = matrix[size - 1 - j][i]
    return rotated_matrix


def create_seq_nxn_matrix(n):
    return [[j for j in range(i, i + n)] for i in range(1, n * n + 1, n)]


class TestMatrixRotation(unittest.TestCase):
    def test_2x2(self):
        original_matrix = create_seq_nxn_matrix(2)
        expected_matrix = [
            [3, 1],
            [4, 2],
        ]
        self.assertEqual(expected_matrix, rotate_90_matrix(original_matrix))

    def test_5x5(self):
        original_matrix = create_seq_nxn_matrix(5)
        expected_matrix = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5],
        ]
        self.assertEqual(expected_matrix, rotate_90_matrix(original_matrix))

    def test_9x9(self):
        original_matrix = create_seq_nxn_matrix(9)
        expected_matrix = [
            [73, 64, 55, 46, 37, 28, 19, 10, 1],
            [74, 65, 56, 47, 38, 29, 20, 11, 2],
            [75, 66, 57, 48, 39, 30, 21, 12, 3],
            [76, 67, 58, 49, 40, 31, 22, 13, 4],
            [77, 68, 59, 50, 41, 32, 23, 14, 5],
            [78, 69, 60, 51, 42, 33, 24, 15, 6],
            [79, 70, 61, 52, 43, 34, 25, 16, 7],
            [80, 71, 62, 53, 44, 35, 26, 17, 8],
            [81, 72, 63, 54, 45, 36, 27, 18, 9],
        ]
        self.assertEqual(expected_matrix, rotate_90_matrix(original_matrix))

    def test_2x3(self):
        original_matrix = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        self.assertRaises(AssertionError, rotate_90_matrix, original_matrix)


if __name__ == "__main__":
    unittest.main()
