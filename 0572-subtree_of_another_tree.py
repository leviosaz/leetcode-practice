# Problem: Find out if the tree defined as subRoot can be found in a "main" tree defined as root.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isSameTree(p, q):
            if p == None or q == None:
                return p == q
        
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        def bfs(main, sub):
            if main == None:
                return
            if isSameTree(main, sub):
                return True
            return bfs(main.left, sub) or bfs(main.right, sub)
        
        return bfs(root, subRoot)

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Side note:
# This can be done slightly more efficiently if done using a stack and iteratively going through all the nodes. 
