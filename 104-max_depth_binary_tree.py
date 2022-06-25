# Problem:
# Find the maximum length of binary tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# Breakdown:
# self.maxDepth ceases when it reaches to its base case, such that the children root does not exist.
# For every case that it doesn't reach to the base case, it keeps adding onto one, getting the maximum subtree with the largest length. 
# For every sub-tree, it keeps adding up to the largest length until we reach to the top.
# In which the maximum length of the two sub trees from the root node + 1 (to include the root node) is our deepest path.

# This is Breadth First Search

# Time Complexity: O(n)
# Space Complexity: O(n)
