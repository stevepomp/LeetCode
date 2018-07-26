'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


#链表结构, divmod(a, b) 返回商和余数

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = temp = ListNode(0)
        m = 0
        while l1 or l2 or m:
            x1 = x2 = 0
            if l1:
                x1 = l1.val
                l1 = l1.next
            if l2:
                x2 = l2.val
                l2 = l2.next
            m, val = divmod(x1+x2+m, 10)
            temp.next = ListNode(val)
            temp = temp.next
        return result.next
