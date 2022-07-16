# Problem: Find a pair of numbers that equal to target number from sorted array.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pointer_l = 0
        pointer_r = len(numbers)-1
        
        while pointer_l < pointer_r:
            tSum = numbers[pointer_l] + numbers[pointer_r] 
            if tSum == target:
                return [pointer_l + 1, pointer_r + 1]
            elif tSum > target:
                pointer_r -= 1
            else:
                pointer_l += 1

# Time Complexity: O(n)
# Space complexity: O(1)
