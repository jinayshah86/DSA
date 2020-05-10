# Q. Implement a function to check if a linked list is a palindrome.
# Solution: Iterative approach using stack
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

    def get_list(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def check_palindrome(self):
        stack = list()
        slow_pointer = self.head
        fast_pointer = self.head
        move_slow_pointer = False
        length = 0
        while fast_pointer:
            fast_pointer = fast_pointer.next
            length += 1
            if move_slow_pointer:
                # Record the first half
                stack.append(slow_pointer.data)
                slow_pointer = slow_pointer.next
            move_slow_pointer = not move_slow_pointer
        # If odd skip the middle element
        if length & 1:
            slow_pointer = slow_pointer.next
        # Match the second half
        while slow_pointer:
            if not stack:
                return False
            if stack.pop() != slow_pointer.data:
                return False
            slow_pointer = slow_pointer.next
        return True


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
