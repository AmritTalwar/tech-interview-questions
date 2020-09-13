# SOURCE: https://leetcode.com/problems/invert-binary-tree/
# And that annoying algoexpert ad on youtube...

# TRIVIA: https://twitter.com/mxcl/status/608682016205344768

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
TIME COMPLEXITY: O(N)
Recursing through each tree node and performing O(1) swaps. We must visit each node to invert the binary tree

SPACE COMPLEXITY: O(N)
Because we are using recurssion, the call stack will reach size H (H = height of tree). In the worse case, the tree is just
one massive branch, so the call stack has a worse case size of N, giving us O(N) space complexity.
"""


def invertBinaryTree(root: TreeNode):
    # We cannot invert a null node, so just return
    if root is None:
        return

    # Swap child nodes of root
    root.left, root.right = root.right, root.left

    # Do the same with the child nodes (i.e. swap their children around)
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)

    return root
