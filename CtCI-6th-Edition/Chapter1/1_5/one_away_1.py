# Q. There are three types of edits that can be performed on strings: insert
# a character, remove a character, or replace a character. Given two strings,
# write a function to check if they are one edit(or zero edits) away.
# Time complexity: O(N); N is the length of the shorter string.
# Space complexity: O(1)

import unittest


def is_one_edit_away(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) >= len(s2):
        short, long = s2, s1
    else:
        short, long = s1, s2
    i = 0
    edit_found = False
    for j in range(len(short)):
        if long[i] != short[j]:
            if len(long) != len(short):
                i += 1
            if edit_found:
                return False
            edit_found = True
        i += 1
    return True


class TestStringCompression(unittest.TestCase):
    def test_pass_1(self):
        self.assertTrue(is_one_edit_away("ple", "pale"))

    def test_pass_2(self):
        self.assertTrue(is_one_edit_away("pales", "pale"))

    def test_pass_3(self):
        self.assertTrue(is_one_edit_away("pale", "bale"))

    def test_fail_1(self):
        self.assertFalse(is_one_edit_away("pale", "bake"))

    def test_fail_2(self):
        self.assertFalse(is_one_edit_away("bakery", "bake"))


if __name__ == "__main__":
    unittest.main()
