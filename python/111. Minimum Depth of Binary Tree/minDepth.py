'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        i = 0
        n = 1
        level, ans = [root], [node for node in (root.left, root.right) if node]
        while root and ans:
            for node in level:
                if not node.left and not node.right:
                    i = 1
                    break
            if i == 1:
                break
            n += 1
            level = ans
            ans = [node for leaf in level for node in (leaf.left, leaf.right) if node]
        return n
