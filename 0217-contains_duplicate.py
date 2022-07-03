# Problem: Check if array has duplicate values.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for x in nums:
            if hashmap.get(x):
                return True
            hashmap[x] = True
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
