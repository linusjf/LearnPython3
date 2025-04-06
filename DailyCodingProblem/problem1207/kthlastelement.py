#!/usr/bin/env python
"""
To solve this problem in one pass and constant space, we can use two pointers that move at the same speed. We'll place the first pointer at the head of the list and the second pointer k steps ahead. Then, we'll move both pointers one step at a time until the second pointer reaches the end of the list. At this point, the first pointer will be at the kth last element.

Here's a Python implementation:
"""
import logging
from typing import Optional
logging.basicConfig(level=logging.WARNING)


class ListNode:
  x: object
  next: Optional['ListNode']
  def __init__(self, x: object):
    self.val: object = x
    self.next: Optional[ListNode] = None

def remove_kth_last(head: Optional[ListNode], k: int) -> Optional[ListNode]:
  if (k < 1):
    logging.warning("k (%d) must be a +ve integer.", k)
    return head

  dummy = ListNode(0)
  dummy.next = head
  first = dummy
  second = dummy

  for _ in range(k + 1):
    if second is not None and second.next is None:
      logging.warning("k (%d) is larger than list length", k)
      return head
    assert second is not None
    second = second.next

  while second:
    assert first.next is not None
    first = first.next
    second = second.next

  assert first.next is not None
  first.next = first.next.next
  return dummy.next

# Example usage
def print_list(head: Optional[ListNode]) -> None:
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
head = remove_kth_last(head, 0)
print("List after attempting removing the 0th last element:")
print_list(head)
head = remove_kth_last(head, -1)
print("List after attempting removing the -1th last element:")
print_list(head)
"""
In this implementation, the `remove_kth_last` function uses two pointers to find the kth last element in the list and removes it. The `print_list` function is used to print the elements of the linked list.

With this implementation, the example usage should produce the correct output.
"""
