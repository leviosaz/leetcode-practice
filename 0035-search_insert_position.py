# Objective:
# Given an array nums:
# if the target exists, return the index
# if the target doesn't, return the index such that if you inserted target there, it would remain sorted.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        beg = 0
        end = len(nums)-1

        if target > nums[end]:
            return end+1
        
        while beg < end:
            mid = (end+beg)//2
            num = nums[mid]
            if num == target:
                return mid
            elif target > num:
                beg = mid+1
            else:
                end = mid
        return beg
        
# Time Complexity: O(log n)
# Space Complexity: O(1)
