# Q. Given two (singly) linked list, determine if the two lists intersect.
# Return the intersecting node. Note that the intersection is defined based on
# reference, not value. That is, the kth node of the first linked list is the
# exact same node (by reference) as the jth node of the second linked list,
# then they are intersecting.
# Time complexity: O(NxM); N and M are the length of the linked list
# Space complexity: O(1)

import operator
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

    def __len__(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next

    def get_list(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __and__(self, other):
        if not isinstance(other, LinkedList):
            raise NotImplementedError
        p1 = self.head
        while p1:
            p2 = other.head
            while p2:
                if p1 is p2:
                    return p1
                p2 = p2.next
            p1 = p1.next
        return None


class TestIntersection(unittest.TestCase):
    def test_intersecting(self):
        n1 = Node(1)
        n2 = Node(2)
        n1.next = n2
        n3 = Node(3)
        n2.next = n3
        n4 = Node(4)
        n5 = Node(5)
        n5.next = n4
        n4.next = n2
        ll1 = LinkedList()
        ll1.head = n5
        ll2 = LinkedList()
        ll2.head = n1
        self.assertIs(n2, operator.and_(ll1, ll2))

    def test_not_intersecting(self):
        n1 = Node(1)
        n2 = Node(2)
        n1.next = n2
        n3 = Node(3)
        n2.next = n3
        n4 = Node(4)
        n5 = Node(5)
        n5.next = n4
        ll1 = LinkedList()
        ll1.head = n5
        ll2 = LinkedList()
        ll2.head = n1
        self.assertIsNone(operator.and_(ll1, ll2))


if __name__ == "__main__":
    unittest.main()
