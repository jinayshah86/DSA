# Q. You have two numbers represented by a linked list, where each node
# contains a single digit. The digits are stored in reverse order, such that
# the 1's digit is at the head of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.
# Example:
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295.
# Output: 2 -> 1 -> 9. That is 912.
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

    def _get_list(self, current):
        while current:
            yield current.data
            current = current.next

    def get_list(self):
        yield from self._get_list(self.head)

    def __len__(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise NotImplementedError
        ll = LinkedList()
        op1 = self.head
        op2 = other.head
        value = 0
        while op1 or op2 or value:
            if op1:
                value += op1.data
                op1 = op1.next
            if op2:
                value += op2.data
                op2 = op2.next
            if value:
                digit = value % 10
                ll.append(digit)
                value //= 10
        return ll


class TestSum(unittest.TestCase):
    def test_empty(self):
        ll1 = LinkedList.create_from_list([])
        ll2 = LinkedList.create_from_list([])
        ll3 = ll1 + ll2
        self.assertEqual([], list(ll3.get_list()))

    def test_pass_1(self):
        ll1 = LinkedList.create_from_list([7, 1, 6])
        ll2 = LinkedList.create_from_list([5, 9, 2])
        ll3 = ll1 + ll2
        self.assertEqual([2, 1, 9], list(ll3.get_list()))

    def test_pass_2(self):
        ll1 = LinkedList.create_from_list([4])
        ll2 = LinkedList.create_from_list([8, 9])
        ll3 = ll1 + ll2
        self.assertEqual([2, 0, 1], list(ll3.get_list()))


if __name__ == "__main__":
    unittest.main()
