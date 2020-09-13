# SOURCE: https://leetcode.com/problems/valid-parentheses/

"""
TIME COMPLEXITY: O(N) N = number of chars in string (or length of the input string)
We go through each bracket and perform O(1) operations.

SPACE COMPLEXITY: O(N)
Worse case the whole string is an unbalanced set of brackets, so we end up with a stack
of size N.
"""


def isValid(bracketString):
    stack = []
    bracketMap = {")": "(", "]": "[", "}": "{"}

    for bracket in bracketString:
        if bracket in bracketMap:
            topStackElement = stack.pop() if stack else "#"
            if bracketMap[bracket] != topStackElement:
                return False
        else:
            stack.append(bracket)

    return not stack
