# Kth Largest Element in a Stream
# Find the kth largest element in a stream. 

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.amt = k
        self.heap = nums
        heapq.heapify(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        
        while len(self.heap) > self.amt:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Time Complexity: O(n logn)
# Space Complexity: O(n)
