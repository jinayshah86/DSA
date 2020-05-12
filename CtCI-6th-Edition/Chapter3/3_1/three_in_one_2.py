# Q.Describe how you could use a single array to implement 3 stacks.
# Space complexity: O(N+K); N is the length of the array, K is the number of
# stacks.
import unittest


class StackInvalid(Exception):
    pass


class StackEmpty(Exception):
    pass


class StackFull(Exception):
    pass


class KStacks:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.stack = [None] * n
        self.top = [-1] * k
        self.next_p = list(range(1, n)) + [-1]
        self.free = 0

    def push(self, elem, sn):
        if self.is_full():
            raise StackFull
        self.check_stack(sn)
        self.stack[self.free] = elem
        self.next_p[self.free], self.free, self.top[sn] = (
            self.top[sn], self.next_p[self.free], self.free)

    def pop(self, sn):
        if self.is_empty(sn):
            raise StackEmpty
        index = self.top[sn]
        val = self.stack[index]
        self.stack[index] = None
        self.top[sn] = self.next_p[index]
        self.next_p[index] = self.free
        self.free = index
        return val

    def peek(self, sn):
        if self.is_empty(sn):
            raise StackEmpty
        return self.stack[self.top[sn]]

    def check_stack(self, sn):
        if sn >= self.k:
            raise StackInvalid

    def is_empty(self, sn):
        self.check_stack(sn)
        return self.top[sn] < 0

    def is_full(self):
        return self.free < 0


class TestKStacks(unittest.TestCase):
    def test_case_1(self):
        st = KStacks(3, 6)
        with self.assertRaises(StackEmpty):
            st.pop(0)
        st.push(1, 0)
        with self.assertRaises(StackEmpty):
            st.pop(1)
        with self.assertRaises(StackEmpty):
            st.pop(2)

    def test_case_2(self):
        st = KStacks(3, 6)
        for i in range(1, 7):
            st.push(i, i % 3)
        self.assertEqual(6, st.pop(0))
        self.assertEqual(4, st.pop(1))
        self.assertEqual(5, st.pop(2))
        self.assertEqual(2, st.pop(2))
        self.assertEqual(1, st.pop(1))
        self.assertEqual(3, st.pop(0))
        for i in range(1, 4):
            st.push(i, i % 3)
        self.assertEqual(2, st.pop(2))
        self.assertEqual(1, st.pop(1))
        self.assertEqual(3, st.pop(0))

    def test_case_3(self):
        st = KStacks(3, 6)
        for i in range(6):
            st.push(i, 0)
        with self.assertRaises(StackFull):
            st.push(6, 0)
        with self.assertRaises(StackFull):
            st.push(6, 1)
        with self.assertRaises(StackFull):
            st.push(6, 2)


if __name__ == '__main__':
    unittest.main()
