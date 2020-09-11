'''This problem is an interactive problem
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, the row is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with atleast 1 in it. If such index does not exist, return -1
You can't access Binary Matrix directly. You may access the matrix using a BinaryMatrix interface:
  >BinaryMatrix.get(x, y) return element of matrix at index x, y (0-indexed)
  >BinaryMatrix.dimensions() returns a list of two elements [n, m] which means the matrix is n*m
Submissions making more than 1000 calls to BinaryMatrix.get will be judged wrong answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
For custom testing purposes you're given binary matrix mat as input in the following four examples. You will not have access to binary matrix directly.

Example 1:                                                Example 2:
0 0                                                       0 0
1 1                                                       0 1
Input: mat = [[0, 0], [1, 1]]                             Input: mat = [[0, 0], [1, 1]]
Output: 0                                                 Output: 1

Example 3:                                                Example 4:
0 0                                                       0 0 0 1
0 0                                                       0 0 1 1
Input: mat = [[0, 0], [0, 0]]                             0 1 1 1
Output: -1                                                Input: mat = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]] 

Constraints:
rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way. '''

class BinaryMatrix(object):
    def get(self, row, col):
        pass
    def dimensions(self):
        pass

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        n, m = binaryMatrix.dimensions()
        res = 1000
        x, y = 0, m - 1
        while x < n and y >= 0:
            if binaryMatrix.get(x, y):
                res = min(res, y)
                y -= 1
            else:
                x += 1
        return -1 if res == 1000 else res









