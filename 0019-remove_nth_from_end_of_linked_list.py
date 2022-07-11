# Problem: Remove the node, that is the nth from the end.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        counter = 0
        traverseNode = head
        resultHead = ListNode(0, head)
        nthFromEndNode = resultHead
        
        while traverseNode:
            counter += 1
            
            if counter > n:
                nthFromEndNode = nthFromEndNode.next        
            
            traverseNode = traverseNode.next
            
        nthFromEndNode.next = nthFromEndNode.next.next
        return resultHead.next

# Time Complexity: O(n)
# Space ComplexitY: O(1)
