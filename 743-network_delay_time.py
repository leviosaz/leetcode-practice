# Minimum Spanning Tree

import collections
import heapq

def networkDelayTime(times, n, k):
    edges = collections.defaultdict(list)
    
    for u, v, w in times:
        edges[u].append((v, w))    

    print(edges)
    
    minHeap = [(0, k)] # (weight, node)
    visited = set()
    t = 0

    # Dijstra's Algorithm:
    while minHeap:
        # Given array of cost it takes to get to get to other points
        # Pop the minimum value. This will be the next point we go to. 
        weight, node = heapq.heappop(minHeap)
        
        # Check if item has already been visited (this means that the edges of this has been accounted for already)
        # Otherwise add to visit
        if node in visited:
            continue
        visited.add(node)
        
        # Add to time t.
        print("============================")
        print(f"T = {t}")
        print(f"Weight = {weight}")
        t = max(t, weight)
    
    
        # Check adjacent edges. 
        for v, w in edges[node]:
            if v not in visited:
                heapq.heappush(minHeap, (w + t, v))
                
        # Look at the nodes outgoing neighbors:
        # If those nodes have been visited, just ignore.
        # Otherwise, get the new cost to go to those points, and then add it to the minHeap

    if len(visited) == n:
        return t 
    return -1
    # After the whole loop is over, if the visited nodes = n return t
    # Otherwise return -1
    

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
