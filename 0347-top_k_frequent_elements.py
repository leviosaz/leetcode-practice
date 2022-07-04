# Problem: Find the top k most frequent items in nums.

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        counter = Counter(nums)
        
        result = [x[0] for x in counter.most_common()][0:k]
        
        return result

# Time Complexity: O(nlogn) (most_common() is a sort function)
# Space Complexity: O(n)
