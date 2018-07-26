'''
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        n = result = ListNode(0)
        l = []
        for i in range(len(lists)):
            if lists[i] != None:
                bisect.insort(l, lists[i].val)
                while lists[i].next:
                    lists[i] = lists[i].next
                    bisect.insort(l, lists[i].val)
        for j in range(len(l)):
            n.next = ListNode(l[j])
            n = n.next
        return result.next
