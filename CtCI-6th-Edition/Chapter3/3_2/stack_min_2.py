# Q. How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum, element? Push, pop and min should all
# operate in O(1) time.
# Time complexity: O(1)
# Space complexity: O(N); N is the size of the stack


import unittest


class StackEmpty(Exception):
    pass


class StackFull(Exception):
    pass


class Stack:
    def __init__(self, size=10):
        self.size = size
        self.stack = []
        self.min_stack = []

    def push(self, elem):
        if self.is_full():
            raise StackFull
        self.stack.append(elem)
        if not self.min_stack:
            self.min_stack.append(elem)
        elif self.min_stack[-1] >= elem:
            self.min_stack.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackEmpty
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def min(self):
        if self.is_empty():
            raise StackEmpty
        return self.min_stack[-1]

    def is_empty(self):
        return not self.stack

    def is_full(self):
        return len(self.stack) == self.size


class TestStackMin(unittest.TestCase):
    def test_case_1(self):
        s = Stack(5)
        with self.assertRaises(StackEmpty):
            s.min()
        s.push(3)
        self.assertEqual(3, s.min())
        s.push(5)
        self.assertEqual(3, s.min())
        s.push(1)
        self.assertEqual(1, s.min())

    def test_case_2(self):
        s = Stack(5)
        s.push(3)
        s.push(5)
        s.push(2)
        s.push(2)
        s.push(1)
        self.assertEqual(1, s.min())
        s.pop()
        self.assertEqual(2, s.min())
        s.pop()
        self.assertEqual(2, s.min())
        s.pop()
        self.assertEqual(3, s.min())
        s.pop()
        self.assertEqual(3, s.min())


if __name__ == '__main__':
    unittest.main()
