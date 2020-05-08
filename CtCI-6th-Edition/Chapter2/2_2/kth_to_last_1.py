# Q. Implement an algorithm to find the kth to last element of a singly linked
# list using two pass approach.
# First pass to calculate the length
# Second pass to reach length - k node
# Time complexity: O(N); N is the length of the linked list
# Space complexity: O(1)

import unittest
from dataclasses import dataclass, field


@dataclass
class Node:
    data: object
    next: object = field(default=None, init=False, repr=False)


@dataclass
class LinkedList:
    head: Node = None

    @classmethod
    def create_from_list(cls, iter):
        ll = LinkedList()
        if not iter:
            return ll
        ll.head = Node(iter[0])
        current = ll.head
        for index in range(1, len(iter)):
            current.next = Node(iter[index])
            current = current.next
        return ll

    def get_list(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    def get_from_last(self, index):
        length = len(self)
        new_index = length - index
        if new_index < 0:
            return None
        current = self.head
        counter = 0
        while current and counter < new_index:
            counter += 1
            current = current.next
        return current.data


class TestKthLast(unittest.TestCase):
    def test_empty(self):
        """Empty linked list"""
        ll = LinkedList.create_from_list([])
        self.assertIsNone(ll.get_from_last(4))

    def test_greater(self):
        """K is greater than length linked list"""
        ll = LinkedList.create_from_list([1, 2])
        self.assertIsNone(ll.get_from_last(3))

    def test_lesser(self):
        """K is lesser than length linked list"""
        ll = LinkedList.create_from_list(list(range(5)))
        self.assertEqual(1, ll.get_from_last(4))


if __name__ == '__main__':
    unittest.main()
