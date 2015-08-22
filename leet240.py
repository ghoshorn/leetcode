# encoding: utf8
'''
Search a 2D Matrix II
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

从左下角开始，如果target比该数小，说明该行不可能有target，上移一行；
如果target比该数打，说明该列不可能有target，右移一列；
如果到右上角还没有target，则返回False.

V.S.
Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

两次二分查找。
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l1=len(matrix)
        if l1==0:
            return False
        l2=len(matrix[0])
        if l2==0:
            return False
        x,y=l1-1,0
        while x>=0 and y<l2:
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]<target:
                y+=1
            elif matrix[x][y]>target:
                x-=1
        return False

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        m=[
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        self.assertEqual(self.a.searchMatrix(m,5),True)
        self.assertEqual(self.a.searchMatrix(m,20),False)


if __name__ == '__main__':
    unittest.main()
