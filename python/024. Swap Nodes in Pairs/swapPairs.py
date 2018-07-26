'''
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = head
        if not n:
            return None

        while n and n.next:
            n.val, n.next.val = n.next.val, n.val
            n = n.next.next
        return head
