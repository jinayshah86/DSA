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

    compressed_string = []
    prev_char = string[0]
    prev_char_count = 1
    for character in string[1:]:
        if character == prev_char:
            prev_char_count += 1
        else:
            compressed_string.append(prev_char)
            compressed_string.append(str(prev_char_count))
            prev_char = character
            prev_char_count = 1

    # Append the trailing similar character(s)
    compressed_string.append(prev_char)
    compressed_string.append(str(prev_char_count))

    # Convert list to string
    compressed_string = "".join(compressed_string)

    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return string


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
