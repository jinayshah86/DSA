# Q. You have two numbers represented by a linked list, where each node
# contains a single digit. The digits are stored in forward order, such that
# the 1's digit is at the tail of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.
# Example:
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295.
# Output: 9 -> 1 -> 2. That is 912.
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

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_padding(self, padding_length, padding_value=0):
        for _ in range(padding_length):
            self.push(padding_value)

    def add_linked_list(self, ll1: Node, ll2: Node, carry: dict):
        new_ll = LinkedList()
        if not (ll1 or ll2):
            return new_ll
        if ll1:
            if ll1.next:
                ll = self.add_linked_list(ll1.next, ll2.next, carry)
                new_ll.head = ll.head
            value = ll1.data + ll2.data + carry["value"]
            carry["value"] = value // 10
            value %= 10
            node = Node(value)
            node.next = new_ll.head
            new_ll.head = node
        return new_ll

    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise NotImplementedError
        l1 = len(self)
        l2 = len(other)
        if l1 > l2:
            other.add_padding(l1 - l2)
        elif l2 > l1:
            self.add_padding(l2 - l1)
        carry = {"value": 0}
        ll = self.add_linked_list(self.head, other.head, carry)
        if carry["value"]:
            node = Node(carry["value"])
            node.next = ll.head
            ll.head = node
        return ll


class TestSum(unittest.TestCase):
    def test_empty(self):
        ll1 = LinkedList.create_from_list([])
        ll2 = LinkedList.create_from_list([])
        ll3 = ll1 + ll2
        self.assertEqual([], list(ll3.get_list()))

    def test_pass_1(self):
        ll1 = LinkedList.create_from_list([6, 1, 7])
        ll2 = LinkedList.create_from_list([2, 9, 5])
        ll3 = ll1 + ll2
        self.assertEqual([9, 1, 2], list(ll3.get_list()))

    def test_pass_2(self):
        ll1 = LinkedList.create_from_list([4])
        ll2 = LinkedList.create_from_list([9, 8])
        ll3 = ll1 + ll2
        self.assertEqual([1, 0, 2], list(ll3.get_list()))

    def test_pass_3(self):
        ll1 = LinkedList.create_from_list([9, 9, 9])
        ll2 = LinkedList.create_from_list([1])
        ll3 = ll1 + ll2
        self.assertEqual([1, 0, 0, 0], list(ll3.get_list()))


if __name__ == '__main__':
    unittest.main()
