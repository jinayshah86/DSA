# Q. Assume you have a method is_substring which checks if one word is a
# substring of another. Given two strings s1 and s2, write code to check if
# s2 is a rotation of s1 using only one call to is_substring(e.g.,
# "waterbottle" is a rotation of "erbottlewat")
# In place of `is_substring` function we'll use in operator for str
# Time complexity: O(N); N is the length of string
# Space complexity: O(N); N is the length of string


import unittest


def is_rotated_string(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s2 in s1 + s1


class TestStringRotation(unittest.TestCase):
    def test_pass(self):
        s1 = "waterbottle"
        s2 = "erbottlewat"
        self.assertTrue(is_rotated_string(s1, s2))

    def test_empty(self):
        self.assertTrue(is_rotated_string("", ""))

    def test_fail_1(self):
        s1 = "waterbottle1"
        s2 = "erbottlewat"
        self.assertFalse(is_rotated_string(s1, s2))

    def test_fail_2(self):
        s1 = "waterbottla"
        s2 = "erbottlewat"
        self.assertFalse(is_rotated_string(s1, s2))


if __name__ == "__main__":
    unittest.main()
