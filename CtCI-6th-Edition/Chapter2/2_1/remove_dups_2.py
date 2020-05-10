# Q. Write code to remove duplicates from an unsorted linked list.
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
        while current is not None:
            yield current.data
            current = current.next

    def remove_dups(self):
        if self.head is None:
            return
        current = self.head
        data_map = {current.data}
        while current and current.next:
            if current.next.data in data_map:
                temp = current.next
                current.next = temp.next
                del temp
            else:
                data_map.add(current.next.data)
                current = current.next


class TestRemoveDuplicates(unittest.TestCase):
    def test_dups_1(self):
        lt = list(map(abs, range(-5, 5)))
        ll = LinkedList.create_from_list(lt)
        ll.remove_dups()
        self.assertEqual(list(range(5, -1, -1)), list(ll.get_list()))

    def test_dups_2(self):
        lt = sorted(list(range(5)) * 3)
        ll = LinkedList.create_from_list(lt)
        ll.remove_dups()
        self.assertEqual(list(range(5)), list(ll.get_list()))

    def test_no_dups(self):
        lt = list(range(5))
        ll = LinkedList.create_from_list(lt)
        ll.remove_dups()
        self.assertEqual(list(range(5)), list(ll.get_list()))

    def test_empty_linked_list(self):
        ll = LinkedList.create_from_list([])
        ll.remove_dups()
        self.assertEqual([], list(ll.get_list()))


if __name__ == "__main__":
    unittest.main()
