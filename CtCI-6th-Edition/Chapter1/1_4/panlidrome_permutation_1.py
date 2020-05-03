# Q. Given a string, write a function to check if it is a permutation of a
# palindrome. A palindrome is a word or phrase that is the same forwards and
# backwards. A permutation is a rearrangement of letters. The palindrome
# does not need to be limited to just dictionary words
# Time complexity: O(N); N is the length of the string.
# Space complexity: O(N); N is the length of the string.

import string as pystring
import unittest

alpha_numeric = pystring.ascii_letters + pystring.digits


def check_palindrome_permutation(
    string: str,
    case_insensitive: bool = True,
    allowed_characters: str = alpha_numeric,
):
    # One can also use collections.Counter or collections.defaultdict(int) as
    # used in CtCI-6th-Edition/Chapter1/1_2/check_permutation.py for
    # simplicity.
    character_map = {}

    for character in string:
        # Skip not allowed characters if allowed_characters is non-empty
        if allowed_characters and character not in allowed_characters:
            continue
        if case_insensitive:
            character = character.lower()
        if character in character_map:
            character_map[character] += 1
        else:
            character_map[character] = 1

    # check if there's at most one odd count character only
    odd_flag = True
    for val in character_map.values():
        if val & 1:  # check if odd
            if not odd_flag:  # another odd count character found
                return False
            odd_flag = False  # mark one odd count character found
    return True


class TestPalindromePermutation(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(check_palindrome_permutation("Tact Coa"))

    def test_fail(self):
        self.assertFalse(check_palindrome_permutation("hello"))


if __name__ == "__main__":
    unittest.main()
