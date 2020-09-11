# SOURCE: https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
TIME COMPLEXITY: O(N)
Worse case there are no cycles, so the fast pointer has to traverse N/2 nodes, giving us a time complexity of O(N). When there is a cycle, 
the slow pointer has to first traverse the non-cyclic length, then at least half the cyclic length before the two pointers meet, giving us a time
complexity again of O(N) (O(non cyclic length + half the cyclic length)).

SPACE COMPLEXITY: O(1)
We are only storing two pointers, constant use of space.
"""


def hasCycle(head: ListNode):
    # Have one slow runner and one fast runner. If there is a cycle, the two will eventually meet.
    # If there is no cycle, the fast runner will eventually reach the end of the linked list.

    # Trivial case where there are no nodes or only one node
    if head is None or head.next is None:
        return False

    slowPointer = head
    fastPointer = head.next

    while slowPointer != fastPointer:
        # If the fastpointer has beyond the end of the list or the last node of the list, we know the list is not cyclic
        if fastPointer is None or fastPointer.next is None:
            return False

        # Slow pointer to move slower than fast pointer
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next

    return True