# Objective:
# Given an array nums, find a pair such that their sum is target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        difference = {}

        for x in range(len(nums)):
            diff = target - nums[x]
            if difference.get(diff) != None:
                return [x, difference[diff]]
            else:
                difference[nums[x]] = x 

# Time Complexity: O(n)
# Space Complexity: O(n)
