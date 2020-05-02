# Q. Given two string, write a method to decide if one if a permutation of the
# other.
# Time complexity: O(N1 + N2); N1 is the length of the string1 and N2 is the
# length of the string2.
# Space complexity: O(N1 + N2); N1 is the length of the string1 and N2 is the
# length of the string2.

import unittest
from collections import Counter, defaultdict


def check_permutation_counter(str1: list, str2: list):
    return Counter(str1) == Counter(str2)


def check_permutation_default_dict(str1: list, str2: list):
    character_map_1 = defaultdict(int)
    character_map_2 = defaultdict(int)
    for character in str1:
        character_map_1[character] += 1
    for character in str2:
        character_map_2[character] += 1
    return character_map_1 == character_map_2


def check_permutation_dict(str1: list, str2: list):
    character_map_1 = {}
    character_map_2 = {}
    for character in str1:
        if character in character_map_1:
            character_map_1[character] += 1
        else:
            character_map_1[character] = 1
    for character in str2:
        if character in character_map_2:
            character_map_2[character] += 1
        else:
            character_map_2[character] = 1
    return character_map_1 == character_map_2


class TestCheckPermutation(unittest.TestCase):
    def test_counter_pass(self):
        self.assertTrue(check_permutation_counter("tac", "cat"))

    def test_counter_fail(self):
        self.assertFalse(check_permutation_counter("mac", "cat"))

    def test_defaultdict_pass(self):
        self.assertTrue(check_permutation_default_dict("tac", "cat"))

    def test_defaultdict_fail(self):
        self.assertFalse(check_permutation_default_dict("mac", "cat"))

    def test_dict_pass(self):
        self.assertTrue(check_permutation_dict("tac", "cat"))

    def test_dict_fail(self):
        self.assertFalse(check_permutation_dict("mac", "cat"))


if __name__ == "__main__":
    unittest.main()
