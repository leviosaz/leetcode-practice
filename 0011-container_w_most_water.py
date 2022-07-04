# Problem: Given an array of heights, find the maximum amount of water. 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start_pointer = 0
        end_pointer = len(height)-1
        maxArea = 0

        while start_pointer < end_pointer:
            maxArea = max(maxArea, min(height[start_pointer], height[end_pointer]) * (end_pointer-start_pointer))

            if height[start_pointer] < height[end_pointer]:
                start_pointer += 1
            else:
                end_pointer -=1

        return maxArea

# Time Complexity: O(n)
# Space Complexity: O(1)
