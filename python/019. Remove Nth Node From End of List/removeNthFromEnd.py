'''
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 1
        hi = lo = head
        while hi.next:
            i += 1
            hi = hi.next
        if i == n:
            return head.next
        for _ in range(i-n-1):
            lo = lo.next
        lo.next = lo.next.next
        return head
