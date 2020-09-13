# SOURCE: https://leetcode.com/problems/move-zeroes/


"""
TIME COMPLEXITY: O(N) N = number of elements in array
Worse case there are no zeroes, so we perform operations on every single element (swapping it with itself). The 'actual' time complexity or best
case is O(numer of non zero elements).

SPACE COMPLEXITY: O(1) Constant space is used.
"""


def moves_zeroes(nums):
    first_zero_index = 0

    # All elements before first_zero_index pointer will be non zeroes, so when we get to a non-zero,
    # swap places with the 0 at first_zero_index and do first_zero_index += 1 as everything between index i and
    # first_zero_index is 0's, so we make the new first_zero_index one after the previous first_zero_index.
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[i], nums[first_zero_index] = nums[first_zero_index], nums[i]
            first_zero_index += 1
    return nums
