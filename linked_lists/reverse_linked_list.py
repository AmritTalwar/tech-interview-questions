# SOURCE: https://leetcode.com/problems/reverse-linked-list/

from ListNode import ListNode

"""
TIME COMPLEXITY: O(N)
We go through each node once and perform O(1) swaps.

SPACE COMPLEXITY: O(1)
"""


def reverse_linked_list(head: ListNode):
    previous = None
    current = head

    while current is not None:
        current_next_temp = current.next
        current.next = previous
        previous = current
        current = current_next_temp

    return previous
