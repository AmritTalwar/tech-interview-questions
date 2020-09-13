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


def in_order_traversal_recursive(root: TreeNode):
    # Need separate traversal function so we can pass through the visited nodes to add to them.
    def traverse(root: TreeNode, visited_nodes):
        if root is not None:
            # traverse through left side, then the root, then the right side, appending to visited_nodes along the way
            if root.left is not None:
                traverse(root.left, visited_nodes)

            visited_nodes.append(root.val)

            if root.right is not None:
                traverse(root.right, visited_nodes)
        return visited_nodes

    traversal_result = traverse(root, [])
    return traversal_result


"""
TIME COMPLEXITY: O(N)
Still iteration through each tree node once.

SPACE COMPLEXITY O(N)
Same as above, but instead its the size of our own 'stack' defined in the function.
"""


def in_order_traversal_iterative(root: TreeNode):
    visited_nodes = []
    stack = []

    current_node = root

    while current_node is not None or len(stack) > 0:
        while current_node is not None:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        visited_nodes.append(current_node.val)
        current_node = current_node.right
