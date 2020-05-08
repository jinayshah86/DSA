# Q. Implement an algorithm to find the kth to last element of a singly linked
# list using two pointers approach.
# Time complexity: O(N); N is the length of the linked list
# Space complexity: O(N); N is the length of the linked list

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

    def get_from_last(self, index):
        forward_pointer = self.head
        backward_pointer = self.head

        # Move forward_pointer k nodes ahead
        for _ in range(index):
            if not forward_pointer:
                return None
            forward_pointer = forward_pointer.next

        # Move forward_pointer till end of linked list and meanwhile also move
        # backward_pointer
        while forward_pointer:
            forward_pointer = forward_pointer.next
            backward_pointer = backward_pointer.next

        return backward_pointer.data


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
