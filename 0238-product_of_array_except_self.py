# Problem: Given an array of numbers, return all of the elements multiplied, except itself.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
    
        preC = 1
        for i in range(len(res)):
            res[i] = preC
            preC *= nums[i]
        postC = 1
        for i in range(len(res)-1, -1, -1):
            res[i] = postC
            postC *= nums[i]
        return res

# Time Complexity: O(n)
# Space Complexity: O(n) 
