# Q. Implement an algorith to determine if a string has all the unique
# characters. What if you cannot use additional data structures?
# Time complexity: O(N^2); N is the length of the string
# Space complexity: O(1)

import unittest


def is_unique(string: str):
    # Have not used string slicing here as it creates a new string
    i = 0
    while i < len(string) - 1:
        j = i + 1
        while j < len(string):
            if string[i] == string[j]:
                return False
            j += 1
        i += 1
    return True


class TestIsUniqueString(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(is_unique("mickey"))

    def test_empty(self):
        self.assertTrue(is_unique(""))

    def test_fail(self):
        self.assertFalse(is_unique("minnie"))


if __name__ == "__main__":
    unittest.main()
