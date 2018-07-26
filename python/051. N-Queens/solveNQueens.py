'''
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        stack, res = [[(0, i)] for i in range(n)], []
        while stack:
            board = stack.pop()
            row = len(board)
            if row == n:
                res.append([''.join('Q' if i == c else '.' for i in range(n))
                            for r, c in board])
            for col in range(n):
                if all(col != c and abs(row-r) != abs(col-c)for r, c in board):
                    stack.append(board+[(row, col)])
        return res
                
