# Q. Write a method to replace all spaces in a string with "%20. You may
# assume that the string has the sufficient space at the end to hold all the
# additional characters, and that you are given the "true" length of the
# string.
# Time complexity: O(N); N is the length of the string.
# Space complexity: O(1)


import unittest


def urlify(string: list):
    # Expecting string as list as they are mutable whether tuple and str
    # are not.
    # Could be done using string method replace or using regex replace but
    # would result in O(N) complexity.
    assert isinstance(string, list)
    for index, character in enumerate(string):
        if character == " ":
            string[index] = "%20"


class TestURLify(unittest.TestCase):
    def test_pass_single_space(self):
        string = list("mickey mouse")
        urlify(string)
        self.assertEqual("".join(string), "mickey%20mouse")

    def test_pass_double_space(self):
        string = list("Mr John Smith")
        urlify(string)
        self.assertEqual("".join(string), "Mr%20John%20Smith")

    def test_assertError(self):
        self.assertRaises(AssertionError, urlify, "mickey mouse")


if __name__ == "__main__":
    unittest.main()
