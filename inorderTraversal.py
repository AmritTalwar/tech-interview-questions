# SOURCE: https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
TIME COMPLEXITY: O(N)
Iterating through each node once when recursing through.

SPACE COMPLEXITY: O(N)
Size of the call stack in the worse case scenario when the binary tree is just one long branch, resulting in 
a call stack of size N.
"""


def inOrderTraversalRecursive(root: TreeNode):
    # Need separate traversal function so we can pass through the visited nodes to add to them.
    def traverse(root: TreeNode, visitedNodes):
        if root is not None:
            # traverse through left side, then the root, then the right side, appending to visitedNodes along the way
            if root.left is not None:
                traverse(root.left, visitedNodes)

            visitedNodes.append(root.val)

            if root.right is not None:
                traverse(root.right, visitedNodes)
        return visitedNodes

    traversalResult = traverse(root, [])
    return traversalResult


"""
TIME COMPLEXITY: O(N)
Still iteration through each tree node once.

SPACE COMPLEXITY O(N)
Same as above, but instead its the size of our own 'stack' defined in the function.
"""


def inOrderTraversalIterative(root: TreeNode):
    visitedNodes = []
    stack = []

    currentNode = root

    while currentNode is not None or len(stack) > 0:
        while currentNode is not None:
            stack.append(currentNode)
            currentNode = currentNode.left
        currentNode = stack.pop()
        visitedNodes.append(currentNode.val)
        currentNode = currentNode.right
