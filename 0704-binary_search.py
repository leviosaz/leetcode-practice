# Problem: Search a sorted array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
                continue
            if nums[mid] > target:
                end = mid - 1
                continue
        return -1

# Time Complexity: O(log n)
# Space Complexity: O(1)
