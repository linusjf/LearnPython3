#!/usr/bin/env python
"""
To solve this problem in one pass and constant space, we can use two pointers that move at the same speed. We'll place the first pointer at the head of the list and the second pointer k steps ahead. Then, we'll move both pointers one step at a time until the second pointer reaches the end of the list. At this point, the first pointer will be at the kth last element.

Here's a Python implementation:
"""
import logging
logging.basicConfig(level=logging.WARNING)


class ListNode:
    val: object
    next: 'ListNode | None'
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_kth_last(head, k):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    for _ in range(k + 1):
      if not second:
        logging.warning("k (%d) is larger than list length", k)
        return head
      second = second.next

    while second:
        assert first.next is not None
        first = first.next
        second = second.next

    assert first.next is not None
    first.next = first.next.next
    return dummy.next

# Example usage
def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
print_list(head)

head = remove_kth_last(head, 2)

print("List after removing the 2nd last element:")
print_list(head)

head = remove_kth_last(head, 8)
print("List after attempting removing the 8th last element:")
print_list(head)
"""
In this implementation, the `remove_kth_last` function uses two pointers to find the kth last element in the list and removes it. The `print_list` function is used to print the elements of the linked list.

With this implementation, the example usage should produce the correct output.
"""
