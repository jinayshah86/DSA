# Q. Implement a function to check if a linked list is a palindrome.
# Solution: Reverse & Compare
# Time complexity: O(N); N is the length of the linked list
# Space complexity: O(N); N is the length of the linked list

from dataclasses import dataclass, field
import unittest


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

    def __len__(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return NotImplementedError
        p1 = self.head
        p2 = other.head
        while p1 or p2:
            if not p1 or not p2:
                return False
            if p1.data != p2.data:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

    def get_list(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def reverse(self):
        ll = LinkedList()
        for element in self.get_list():
            ll.push(element)
        return ll

    def check_palindrome(self):
        ll = self.reverse()
        return self == ll


class TestPalindrome(unittest.TestCase):
    def test_empty(self):
        ll = LinkedList.create_from_list([])
        self.assertTrue(ll.check_palindrome())

    def test_true_odd(self):
        ll = LinkedList.create_from_list([1, 2, 3, 2, 1])
        self.assertTrue(ll.check_palindrome())

    def test_true_even(self):
        ll = LinkedList.create_from_list([1, 2, 2, 1])
        self.assertTrue(ll.check_palindrome())

    def test_false_odd(self):
        ll = LinkedList.create_from_list([1, 2, 3, 3, 1])
        self.assertFalse(ll.check_palindrome())

    def test_false_even(self):
        ll = LinkedList.create_from_list([1, 2, 3, 1])
        self.assertFalse(ll.check_palindrome())


if __name__ == '__main__':
    unittest.main()
