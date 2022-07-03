# Problem: Given a series of points, give the k closest points closest to the origin

from bisect import insort

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        for x in points:
            dist = x[0]**2 + x[1]**2
            result.append([dist, x])

        return [y[1] for y in sorted(result, key = lambda x: x[0])][0:k]

# Time Complexity: O(n)
# Space Complexity: O(n)
