# SOURCE: https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        TIME COMPLEXITY: O(N)
        Iterating through N objects performing O(1) operations

        SPACE COMPLEXITY: O(N)
        Worst case scenario we end up with a hashmap with N - 1 entries
        (one of the pair nums is at the end of the array)
        """

        complements_dict = {}

        for i in range(0, len(nums)):  # O(N) iteration through array
            number = nums[i]
            number_compliment = target - number

            if number_compliment not in complements_dict:  # O(1) hashmap lookup
                complements_dict[number] = i
            else:
                return [i, complements_dict[number_compliment]]
