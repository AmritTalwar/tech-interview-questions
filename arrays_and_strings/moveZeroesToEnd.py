# SOURCE: https://leetcode.com/problems/move-zeroes/


"""
TIME COMPLEXITY: O(N) N = number of elements in array
Worse case there are no zeroes, so we perform operations on every single element (swapping it with itself). The 'actual' time complexity or best
case is O(numer of non zero elements).

SPACE COMPLEXITY: O(1) Constant space is used.
"""


def moveZeroes(nums):
    firstZeroIndex = 0

    # All elements before firstZeroIndex pointer will be non zeroes, so when we get to a non-zero,
    # swap places with the 0 at firstZeroIndex and do firstZeroIndex += 1 as everything between index i and
    # firstZeroIndex is 0's, so we make the new firstZeroIndex one after the previous firstZeroIndex.
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[i], nums[firstZeroIndex] = nums[firstZeroIndex], nums[i]
            firstZeroIndex += 1
    return nums
