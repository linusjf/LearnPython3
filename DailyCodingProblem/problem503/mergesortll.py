#!/usr/bin/env python
"""
Mergesortll.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : mergesortll
# @created     : Tuesday Mar 28, 2023 22:29:41 IST
# @description : Python3 program to merge sort of linked list
# -*- coding: utf-8 -*-'
######################################################################
"""
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    """Define node class."""

    data: Any = None
    next: Optional["Node"] = None


class LinkedList:
    """Define linked list class."""

    def __init__(self):
        """Initialise."""
        self.head = None

    # push new value to linked list
    # using append method
    def append(self, new_value):
        """Append."""
        # Allocate new node
        new_node = Node(new_value)
        # if head is None, initialize it to new node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        # Append the new node at the end
        # of the linked list
        curr_node.next = new_node

    def sorted_merge(self, start, end):
        """Merge."""
        result = None
        # Base cases
        if start is None:
            return end
        if end is None:
            return start
        # pick either a or b and recur..
        if start.data <= end.data:
            result = start
            result.next = self.sorted_merge(start.next, end)
        else:
            result = end
            result.next = self.sorted_merge(start, end.next)
        return result

    def merge_sort(self, head):
        """Merge sort."""
        # Base case if head is None
        if head is None or head.next is None:
            return head
        # get the middle of the list
        middle = self.get_middle(head)
        nexttomiddle = middle.next
        # set the next of middle node to None
        middle.next = None
        # Apply mergeSort on left list
        left = self.merge_sort(head)
        # Apply mergeSort on right list
        right = self.merge_sort(nexttomiddle)
        # Merge the left and right lists
        sortedlist = self.sorted_merge(left, right)
        return sortedlist

    # Utility function to get the middle
    # of the linked list
    def get_middle(self, head):
        """Compute center of list."""
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


# Utility function to print the linked list
def print_list(head):
    """Print list."""
    if head is None:
        print(" ")
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(" ")


# Driver Code
if __name__ == "__main__":
    li = LinkedList()
    # Let us create a unsorted linked list
    # to test the functions created.
    # The list shall be a: 2->3->20->5->10->15
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)
    # Apply merge Sort
    li.head = li.merge_sort(li.head)
    print("Sorted Linked List is:")
    print_list(li.head)
