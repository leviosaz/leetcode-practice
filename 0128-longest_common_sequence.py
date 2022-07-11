# Problem: Find the longest consecutive sequence in array.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        longest = 0

        for x in nums:
            if x - 1 not in nums:
                length = 0
                while x + length in nums:
                    length += 1
                longest = max(longest, length)

        return longest

# Time Complexity: O(n) 
# Space Complexity: O(n)
