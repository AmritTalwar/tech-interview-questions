# SOURCE: https://leetcode.com/problems/valid-parentheses/

"""
TIME COMPLEXITY: O(N) N = number of chars in string (or length of the input string)
We go through each bracket and perform O(1) operations.

SPACE COMPLEXITY: O(N)
Worse case the whole string is an unbalanced set of brackets, so we end up with a stack
of size N.
"""


def is_valid(bracket_string):
    stack = []
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for bracket in bracket_string:
        if bracket in bracket_map:
            top_stack_element = stack.pop() if stack else "#"
            if bracket_map[bracket] != top_stack_element:
                return False
        else:
            stack.append(bracket)

    return not stack
