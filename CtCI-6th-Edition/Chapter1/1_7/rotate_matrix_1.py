# Q. Given an image represented by an NxN matrix, where each pixel in the
# image is 4 bytes, writes a method ot rotate the image by 90 degrees. Can
# you do this in place?
# Time complexity: O(N^2); N is the size of the NxN matrix.
# Space complexity: O(N^2); N is the size of the NxN matrix.

import unittest


def rotate_90_matrix(matrix):
    return list(map(list, zip(*matrix[::-1])))


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

    def test_4x4(self):
        original_matrix = create_seq_nxn_matrix(4)
        expected_matrix = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4],
        ]
        self.assertEqual(expected_matrix, rotate_90_matrix(original_matrix))


if __name__ == "__main__":
    unittest.main()
