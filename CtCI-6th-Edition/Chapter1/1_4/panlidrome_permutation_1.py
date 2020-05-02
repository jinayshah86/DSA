# Q. Given a string, write a function to check if it is a permutation of a
# palindrome. A palindrome is a word or phrase that is the same forwards and
# backwards. A permutation is a rearrangement of letters. The palindrome
# does not need to be limited to just dictionary words
# Time complexity: O(N); N is the length of the string.
# Space complexity: O(N); N is the length of the string.

# Assumptions A1: Palindrome to checked only for alpha numeric characters. Remove
# wihte spaces, puntuations or any other special characters.

import unittest


def check_palindrome_permutation(string: str):
    # One can also use collections.Counter or collections.defaultdict(int) as
    # used in CtCI-6th-Edition/Chapter1/1_2/check_permutation.py for
    # simplicity.
    character_map = {}

    for character in string:
        if not character.isalnum():  # Assumption A1
            continue
        # while checking for palindrom case of the character won't matter as
        # 'a' is considered equivalent to 'A'
        character = character.lower()
        if character in character_map:
            character_map[character] += 1
        else:
            character_map[character] = 1

    odd_flag = True  # to check if there's at most on odd only
    for val in character_map.values():
        if val % 2 != 0:
            if odd_flag:
                odd_flag = False
            else:
                return False
    return True


class TestPalindromePermutation(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(check_palindrome_permutation("Tact Coa"))

    def test_fail(self):
        self.assertFalse(check_palindrome_permutation("hello"))


if __name__ == "__main__":
    unittest.main()
