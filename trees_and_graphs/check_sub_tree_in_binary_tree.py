# SOURCE: https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
TIME COMPLEXITY: O(N * M) N = number of nodes in tree S, M = number of nodes in tree T
For every single node in tree S, we make a maximum of M comparrisons (compare against each node in T).

SPACE COMPLEXITY: O(min(N, M))
The recurssion stack can only grow as big as the tree with the least amount of nodes.
"""


def is_subtree(s, t):
    # if the main tree node is null, then there cannot be a subtree of a null node, so return false
    if s is None:
        return False

    # check if tree starting at node S is the same as our subtree T
    elif is_sametree(s, t):
        return True

    # else, check if the left and right halfs of the main tree to see if tree T is within these trees
    else:
        return is_subtree(s.left, t) or is_subtree(s.right, t)


def is_sametree(s, t):
    # when we have reached the end of one tree branch, check if we have reached the end of the other tree as well
    if s is None or t is None:
        return s is None and t is None

    # current tree nodes match, so check if the left and right nodes match to make sure the full subtree matches
    elif s.val == t.val:
        return is_sametree(s.left, t.left) and is_sametree(s.right, t.right)
    else:
        return False
