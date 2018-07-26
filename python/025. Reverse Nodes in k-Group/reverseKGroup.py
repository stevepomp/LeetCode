'''
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if k == 1:
            return head
        m = head
        n = result = ListNode(0)
        i = 1
        l = array.array('I', [m.val])
        s = array.array('I')
        while m.next:
            i += 1
            m = m.next
            l.append(m.val)
        a, b = divmod(i, k)
        for x in range(1, a+1):
            temp = l[(x-1)*k:x*k]
            temp.reverse()
            for y in temp:
                s.append(y)
        if b != 0:
            for z in l[-b:]:
                s.append(z)
        for j in s:
            n.next = ListNode(j)
            n = n.next
        return result.next
