# Q. Given a circular linked list, implement an algorithm that returns the
# node at the beginning of the loop.
# DEFINITION:
# Circular linked list: A (corrupt) linked list in which a node's next pointer
# points to an earlier node, so as to make a loop in the linked list.
# EXAMPLE:
# Input: A -> B -> C -> D -> E -> C (the same C as earlier)
# Output: C
# Time complexity: O(N); N is the length of the linked list
# Space complexity: O(N); N is the length of the linked list


import unittest
from dataclasses import dataclass, field


@dataclass
class Node:
    data: object
    next: object = field(default=None, init=False, repr=False)

    def __hash__(self):
        return id(self)


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

    def detect_loop(self):
        hash_set = set()
        current = self.head
        while current:
            if current in hash_set:
                return current
            hash_set.add(current)
            current = current.next
        return None


class TestLoopDetection(unittest.TestCase):
    def test_loop_1(self):
        ll = LinkedList()
        ll.head = Node(0)
        ll.head.next = Node(1)
        ll.head.next.next = Node(2)
        n3 = Node(3)
        ll.head.next.next.next = n3
        n3.next = Node(4)
        n3.next.next = Node(5)
        n3.next.next.next = n3
        self.assertIs(n3, ll.detect_loop())

    def test_loop_2(self):
        ll = LinkedList()
        ll.head = Node(0)
        n1 = Node(1)
        ll.head.next = n1
        ll.head.next.next = Node(2)
        ll.head.next.next.next = Node(3)
        ll.head.next.next.next.next = Node(4)
        ll.head.next.next.next.next.next = n1
        self.assertIs(n1, ll.detect_loop())

    def test_no_loop(self):
        ll = LinkedList()
        ll.head = Node(0)
        ll.head.next = Node(1)
        ll.head.next.next = Node(2)
        n3 = Node(3)
        ll.head.next.next.next = n3
        n3.next = Node(4)
        n3.next.next = Node(5)
        self.assertIsNone(ll.detect_loop())


if __name__ == "__main__":
    unittest.main()
