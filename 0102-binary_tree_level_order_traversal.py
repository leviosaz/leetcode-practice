# Problem: Given a binary tree, return all the layers of it in their separate lists
# In level order order. 

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        queue = deque()
        queue.append(root)

        result = []
        
        while queue:
            tmpResult = []
            tmpLayer = []
            while queue:
                x = queue.popleft()
                try:
                    tmpLayer.extend([x.left, x.right])
                    tmpResult.append(x.val)
                except AttributeError:
                    pass
            if tmpResult: 
                result.append(tmpResult)
            queue.extend(tmpLayer)
        
        return result
            
# Time Complexity: O(n) - n being the amount of nodes in the tree
# Space Complexity: O(n)
