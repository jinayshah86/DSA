# Q. Imagine a (literal) stack of plates. If the stack gets too high, it might
# topple. Therefore, in real life, we would likely start a new stack when the
# previous stack exceeds some threshold. Implement a data structure
# SetOfStacks that mimics this. SetofStacks should be composed of several
# stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a
# single stack(that is pop() should return the same values as it would if
# there were just a single stack).
# Time complexity: O(1)
# Space complexity: O(1)

import unittest


class StackEmpty(Exception):
    pass


class SetOfStacks:
    def __init__(self, size):
        self.size = size
        self.stacks = []

    def get_last_stack(self):
        if self.is_empty():
            return None
        return self.stacks[-1]

    def is_stack_full(self, stack):
        if stack and len(stack) == self.size:
            return True
        return False

    def push(self, elem):
        stack = self.get_last_stack()
        if not stack or self.is_stack_full(stack):
            stack = []
            self.stacks.append(stack)
        stack.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackEmpty
        stack = self.stacks[-1]
        val = stack.pop()
        if not stack:
            self.stacks.pop()
        return val

    def is_empty(self):
        return not self.stacks


class TestSetOfStacks(unittest.TestCase):
    def test_push_pop(self):
        st = SetOfStacks(3)
        with self.assertRaises(StackEmpty):
            st.pop()
        st.push(1)
        self.assertEqual(1, st.pop())
        with self.assertRaises(StackEmpty):
            st.pop()

    def test_overflow(self):
        st = SetOfStacks(3)
        for i in range(7):
            st.push(i)
        self.assertEqual(3, len(st.stacks))
        self.assertEqual(6, st.pop())
        self.assertEqual(2, len(st.stacks))
        for i in reversed(range(6)):
            self.assertEqual(i, st.pop())
        self.assertTrue(st.is_empty())
        self.assertEqual(0, len(st.stacks))


if __name__ == "__main__":
    unittest.main()
