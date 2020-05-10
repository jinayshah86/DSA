# Q. Write a code to partition a linked list around a value x, such that all
# nodes less than x come before all nodes greater than or equal to x. If x is
# contained within the list, the values of x only need to be after the elements
# less than x. You should preserve the original relative order of the nodes in
# each of the two partitions.
# Example:
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
# Output: 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10
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

    def partition(self, value):
        ll_front_current = Node(0)
        ll_back_current = Node(0)
        ll_front = LinkedList(head=ll_front_current)
        ll_back = LinkedList(head=ll_back_current)
        current = self.head
        # Generate front and back linked list
        while current:
            if current.data < value:
                ll_front_current.next = Node(current.data)
                ll_front_current = ll_front_current.next
            else:
                ll_back_current.next = Node(current.data)
                ll_back_current = ll_back_current.next
            current = current.next
        # Merge front and back linked list
        ll_front_current.next = ll_back.head.next
        return LinkedList(head=ll_front.head.next)


class TestPartition(unittest.TestCase):
    def test_empty(self):
        """Empty linked list"""
        ll = LinkedList.create_from_list([])
        partition_value = 1
        partitioned_ll = ll.partition(partition_value)
        self.assertEqual([], list(partitioned_ll.get_list()))

    def test_pass_1(self):
        ll = LinkedList.create_from_list([1])
        partition_value = 5
        partitioned_ll = ll.partition(partition_value)
        self.assertEqual([1], list(partitioned_ll.get_list()))

    def test_pass_2(self):
        ll = LinkedList.create_from_list([5, 3, 6, 4, 2, 1])
        partition_value = 4
        partitioned_ll = ll.partition(partition_value)
        self.assertEqual([3, 2, 1, 5, 6, 4], list(partitioned_ll.get_list()))

    def test_pass_3(self):
        ll = LinkedList.create_from_list([3, 5, 8, 5, 10, 2, 1])
        partition_value = 5
        partitioned_ll = ll.partition(partition_value)
        self.assertEqual([3, 2, 1, 5, 8, 5, 10],
                         list(partitioned_ll.get_list()))


if __name__ == "__main__":
    unittest.main()
