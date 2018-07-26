'''
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = []
        n = result = ListNode(0)
        if l1:
            bisect.insort(l, l1.val)
            while l1.next:
                l1 = l1.next
                bisect.insort(l, l1.val)
        if l2:
            bisect.insort(l, l2.val)
            while l2.next:
                l2 = l2.next
                bisect.insort(l, l2.val)
        if l:
            for x in l:
                n.next = ListNode(x)
                n = n.next
        return result.next
