# Q. Implement a MyQueue class which implements a queue using two stacks.
# Enqueue is costly
# Time complexity: O(1); Amortized(1) complexity
# Space complexity: O(N); N is the length of queue

import unittest


class StackEmpty(Exception):
    pass


class QueueEmpty(Exception):
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


class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, elem):
        # Push new element to s1
        self.s1.push(elem)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty
        if not self.s2.is_empty():
            return self.s2.pop()
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()


class TestMyQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = MyQueue()
        for i in range(5):
            q.enqueue(i)

        for i in range(5):
            self.assertEqual(i, q.dequeue())

    def test_queue_empty(self):
        q = MyQueue()
        with self.assertRaises(QueueEmpty):
            q.dequeue()


if __name__ == "__main__":
    unittest.main()
