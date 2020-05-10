# Q. Implement an algorithm to delete a node in the middle(i.e., any node but
# the first and last node not necessarily the exact middle) of a singly linked
# list, given only access to that node
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

    def delete_middle(self):
        if not self.head:
            return
        previous_pointer = None
        slow_pointer = self.head
        fast_pointer = self.head
        # Move fast_pointer till end of the linked_list
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            previous_pointer = slow_pointer
            slow_pointer = slow_pointer.next
        if previous_pointer is not None:
            previous_pointer.next = slow_pointer.next
        else:
            self.head = None
        del slow_pointer


class TestDeleteMiddle(unittest.TestCase):
    def test_empty(self):
        """Empty linked list"""
        ll = LinkedList.create_from_list([])
        ll.delete_middle()
        self.assertEqual([], list(ll.get_list()))

    def test_odd_1(self):
        ll = LinkedList.create_from_list([1])
        ll.delete_middle()
        self.assertEqual([], list(ll.get_list()))

    def test_odd_2(self):
        ll = LinkedList.create_from_list([1, 2, 3])
        ll.delete_middle()
        self.assertEqual([1, 3], list(ll.get_list()))

    def test_odd_3(self):
        ll = LinkedList.create_from_list([1, 2, 3, 4, 5])
        ll.delete_middle()
        self.assertEqual([1, 2, 4, 5], list(ll.get_list()))

    def test_even_1(self):
        ll = LinkedList.create_from_list([1, 2])
        ll.delete_middle()
        self.assertEqual([1], list(ll.get_list()))

    def test_even_2(self):
        ll = LinkedList.create_from_list([1, 2, 3, 4])
        ll.delete_middle()
        self.assertEqual([1, 2, 4], list(ll.get_list()))

    def test_even_3(self):
        ll = LinkedList.create_from_list([1, 2, 3, 4, 5, 6])
        ll.delete_middle()
        self.assertEqual([1, 2, 3, 5, 6], list(ll.get_list()))


if __name__ == "__main__":
    unittest.main()
