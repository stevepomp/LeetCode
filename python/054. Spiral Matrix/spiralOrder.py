'''
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix:
            while matrix and matrix[0]:
                result += [matrix[0].pop(0)]
            while matrix and matrix[0] == []:
                matrix.pop(0)
            if matrix:
                for i in range(len(matrix)):
                    result += [matrix[i].pop()]
            while matrix and matrix[-1]:
                result += [matrix[-1].pop()]
            while matrix and matrix[-1] == []:
                matrix.pop()
            if matrix:
                for i in range(len(matrix)-1, -1, -1):
                    result += [matrix[i].pop(0)]
        return result
