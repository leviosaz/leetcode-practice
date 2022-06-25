from heapq import heapify, heappop

class Solution(object):

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # Creating the hashmap
        edges = []

        length = len(points)

        # Fill up the Hashmap with every path
        for start in range(length):
            for end in range(start + 1, length):
                if start == end:
                    continue
                distance = abs((points[start][0]-points[end][0])) + abs((points[start][1]-points[end][1]))
                edges.append((distance, start, end))

        edges.sort()

        # Indexes reference the point, and the value in the indexes references the group they're in.
        # A set where all are equal (e.g. [0, 0, 0, 0, 0]) is a set where all the points are in the same set
        # Meaning that they are connected. 

        roots = [i for i in range(length)]

        def find(v):
            # Given a vertices v, this recursion finds which group the v belongs to.

            # The roots start off with [0, 1, 2, 3, 4,..., n]. All indexes start in their own separate groups
            # If the roots[v] (the group) is different from v (the element), that means it has been associated with a different group
            # The recursion returns the group an element is in

            if roots[v] != v:
                roots[v] = find(roots[v])
            return roots[v]

        def union(u, v):
            p1 = find(u)
            p2 = find(v)

            # If the two elements are in different groups, we put them into the same group.
            # We then return True to signify the loop below to add to the distance 
            # As this means that a new point has been added to the graph successfully. 
            if p1 != p2:
                roots[p2] = roots[p1]
                return True
            return False

        distance = 0
        for d, u, v in edges:
            if union(u, v):
                distance += d
        return distance

