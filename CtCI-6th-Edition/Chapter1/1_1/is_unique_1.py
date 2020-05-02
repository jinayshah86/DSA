# Q. Implement an algorith to determine if a string has all the unique
# characters. What if you cannot use additional data structures?
# Time complexity: O(N); N is the length of the string
# Space complexity: O(N): N is the length of the string

import unittest


def is_unique(string: str):
    character_map = {}
    for character in string:
        if character in character_map:
            return False
        character_map[character] = True
    return True


class TestIsUniqueString(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(is_unique("mickey"))

    def test_fail(self):
        self.assertFalse(is_unique("minnie"))


if __name__ == "__main__":
    unittest.main()
