# Q. Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string 'aabcccccaaa' would become
# 'a2b1c5a3'. If the "compressed" string would not become smaller than the
# original string, your method should return the original string. You can
# assume the string has only uppercase and lowercase letter (a-z).
# Time complexity: O(N); N is the length of the string.
# Space complexity: O(N); N is the length of the string.

import unittest


def string_compression(string: str) -> str:
    # Check for empty string
    if not string:
        return string
    # Check for string with alphabets only
    if not string.isalpha():
        raise ValueError

    compressed_str = []
    char_count = 0
    for index, character in enumerate(string):
        char_count += 1
        if (index + 1) >= len(string) or character != string[index + 1]:
            compressed_str.append(character)
            compressed_str.append(str(char_count))
            char_count = 0

    # Convert list to string
    compressed_str = "".join(compressed_str)

    return compressed_str if len(compressed_str) < len(string) else string


class TestStringCompression(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(string_compression("aabcccccaaa"), "a2b1c5a3")

    def test_uncompress(self):
        self.assertEqual(string_compression("mickey"), "mickey")

    def test_exception(self):
        self.assertRaises(ValueError, string_compression, "a2b1c5a3")

    def test_empty(self):
        self.assertEqual(string_compression(""), "")


if __name__ == "__main__":
    unittest.main()
