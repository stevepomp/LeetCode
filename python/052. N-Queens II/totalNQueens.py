'''
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack, result = [[(0, i)] for i in range(n)], 0
        while stack:
            board = stack.pop()
            row = len(board)
            if row == n:
                result += 1
            for col in range(n):
                if all(col != c and abs(col-c) != abs(row-r) for r, c in board):
                    stack.append(board+[(row, col)])
        return result
