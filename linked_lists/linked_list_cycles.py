# SOURCE: https://leetcode.com/problems/linked-list-cycle

from ListNode import ListNode

"""
TIME COMPLEXITY: O(N)
Worse case there are no cycles, so the fast pointer has to traverse N/2 nodes, giving us a time complexity of O(N). When there is a cycle, 
the slow pointer has to first traverse the non-cyclic length, then at least half the cyclic length before the two pointers meet, giving us a time
complexity again of O(N) (O(non cyclic length + half the cyclic length)).

SPACE COMPLEXITY: O(1)
We are only storing two pointers, constant use of space.
"""


def has_cycle(head: ListNode):
    # Have one slow runner and one fast runner. If there is a cycle, the two will eventually meet.
    # If there is no cycle, the fast runner will eventually reach the end of the linked list.

    # Trivial case where there are no nodes or only one node
    if head is None or head.next is None:
        return False

    slow_pointer = head
    fast_pointer = head.next

    while slow_pointer != fast_pointer:
        # If the fast_pointer has beyond the end of the list or the last node of the list, we know the list is not cyclic
        if fast_pointer is None or fast_pointer.next is None:
            return False

        # Slow pointer to move slower than fast pointer
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return True