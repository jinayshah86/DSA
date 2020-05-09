# Q. Write a code to partition a linked list around a value x, such that all
# nodes less than x come before all nodes greater than or equal to x. If x is
# contained within the list, the values of x only need to be after the elements
# less than x. The partition element x can appear anywhere in the "right
# partition"; it does not need to appear between the left and right partitions.
# Example:
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
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
        ll = LinkedList()
        if not self.head:
            return ll
        ll.head = Node(self.head.data)
        tail = ll.head
        for element in self._get_list(self.head.next):
            if element >= value:
                tail.next = Node(element)
                tail = tail.next
            else:
                node = Node(element)
                node.next = ll.head
                ll.head = node
        return ll


class TestPartition(unittest.TestCase):
    def partition_test(self, ll, value):
        partitioned_ll = ll.partition(value)
        left_partition = True
        for element in partitioned_ll.get_list():
            if element < value:
                self.assertTrue(left_partition)
            else:
                left_partition = False
        self.assertEqual(len(ll), len(partitioned_ll))

    def test_empty(self):
        """Empty linked list"""
        ll = LinkedList.create_from_list([])
        partition_value = 1
        self.partition_test(ll, partition_value)

    def test_pass_1(self):
        ll = LinkedList.create_from_list([1])
        partition_value = 5
        self.partition_test(ll, partition_value)

    def test_pass_2(self):
        ll = LinkedList.create_from_list([1, 5, 3, 6, 4, 2])
        partition_value = 4
        self.partition_test(ll, partition_value)

    def test_pass_3(self):
        ll = LinkedList.create_from_list([3, 5, 8, 5, 10, 2, 1])
        partition_value = 5
        self.partition_test(ll, partition_value)


if __name__ == '__main__':
    unittest.main()
