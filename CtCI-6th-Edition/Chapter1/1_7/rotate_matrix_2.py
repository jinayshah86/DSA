# Q. Given an image represented by an NxN matrix, where each pixel in the
# image is 4 bytes, writes a method ot rotate the image by 90 degrees. Can
# you do this in place?
# Time complexity: O(N^2); N is the size of the NxN matrix.
# Space complexity: O(1)

import unittest


def rotate_90_matrix(matrix):
    size = len(matrix)
    # validation in O(N)
    for row in matrix:
        assert len(row) == size
    if size == 1:  # Identity case
        return
    mid = max(1, size // 2)
    for i in range(mid):
        for j in range(i, size - 1 - i):
            (
                matrix[i][j],
                matrix[j][size - 1 - i],
                matrix[size - 1 - i][size - 1 - j],
                matrix[size - 1 - j][i],
            ) = (
                matrix[size - 1 - j][i],
                matrix[i][j],
                matrix[j][size - 1 - i],
                matrix[size - 1 - i][size - 1 - j],
            )


def create_seq_nxn_matrix(n):
    return [[j for j in range(i, i + n)] for i in range(1, n * n + 1, n)]


class TestMatrixRotation(unittest.TestCase):
    def test_2x2(self):
        original_matrix = create_seq_nxn_matrix(2)
        expected_matrix = [
            [3, 1],
            [4, 2],
        ]
        rotate_90_matrix(original_matrix)
        self.assertEqual(expected_matrix, original_matrix)

    def test_5x5(self):
        original_matrix = create_seq_nxn_matrix(5)
        expected_matrix = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5],
        ]
        rotate_90_matrix(original_matrix)
        self.assertEqual(expected_matrix, original_matrix)

    def test_2x3(self):
        original_matrix = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        self.assertRaises(AssertionError, rotate_90_matrix, original_matrix)

    def test_4x4(self):
        original_matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16],
        ]
        expected_matrix = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11],
        ]
        rotate_90_matrix(original_matrix)
        self.assertEqual(expected_matrix, original_matrix)


if __name__ == "__main__":
    unittest.main()
