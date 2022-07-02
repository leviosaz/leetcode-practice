# Problem:
# Merge two sorted linked lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        pointer = head

        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = ListNode(list1.val)
                list1 = list1.next
            else:
                pointer.next = ListNode(list2.val)
                list2 = list2.next
            pointer = pointer.next

        if list1:
            pointer.next = list1
        if list2:
            pointer.next = list2

        return head.next

# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
