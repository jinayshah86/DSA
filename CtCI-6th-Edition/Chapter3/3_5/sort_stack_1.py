# Q. Write a program to sort a stack such that the smallest items are on the
# top. You can use an additional temporary stack, but you may not copy the
# elements into any other data structure (such as an array). The stack
# supports the following operations: push, pop, peek, and is_empty.
# Time complexity: O(N^2); N is the length of the stack
# Space complexity: O(N); N is the length of the stack

import unittest
from random import shuffle


class StackEmpty(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackEmpty
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise StackEmpty
        return self.stack[-1]

    def is_empty(self):
        return not self.stack


class SortStack:
    def __init__(self):
        self.s1 = Stack()  # primary stack
        self.s2 = Stack()  # temporary stack

    def push(self, elem):
        # Transfer elements from s1 to s2 till s1 is empty or element at the
        # top of s1 stack is greater than or equal to element to be pushed
        while not self.s1.is_empty() and self.s1.peek() < elem:
            self.s2.push(self.s1.pop())
        # Push the new element
        self.s1.push(elem)
        # Transfer all the elements from s2 back to s1
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())

    def pop(self):
        if self.is_empty():
            raise StackEmpty
        return self.s1.pop()

    def is_empty(self):
        return not self.s1


class TestSortStack(unittest.TestCase):
    def test_case_1(self):
        l = list(range(5))
        shuffle(l)  # Randomize order of the list
        s = SortStack()
        for i in l:
            s.push(i)
        for i in range(5):
            self.assertEqual(i, s.pop())

    def test_empty(self):
        s = SortStack()
        with self.assertRaises(StackEmpty):
            s.pop()


if __name__ == "__main__":
    unittest.main()
