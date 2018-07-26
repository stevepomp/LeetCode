'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level, result = [root], []
        while root and level:
            result.append([node.val for node in level])
            level = [node for leaf in level for node in (leaf.left, leaf.right) if node]
            result.append([node.val for node in reversed(level)])
            level = [node for leaf in level for node in (leaf.left, leaf.right) if node]
        if result and result[-1] == []:
            result.pop()
        return result
