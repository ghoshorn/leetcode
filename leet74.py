# encoding: utf8
'''
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

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        l1=len(matrix)
        l2=len(matrix[0])
        if target<matrix[0][0] or target>matrix[l1-1][l2-1]:
            return False
        start =0
        end   =l1-1
        while start<=end:
            mid=(start+end)/2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]>target:
                end=mid-1
            else:
                start=mid+1
        if matrix[mid][0]>target:
            mid-=1
        row=mid
        start =0
        end   =l2-1
        while start<=end:
            mid=(start+end)/2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                end=mid-1
            else:
                start=mid+1
        return False

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.searchMatrix([
                                              [1,   3,  5,  7],
                                              [10, 11, 16, 20],
                                              [23, 30, 34, 50]
                                            ],3),True)
        self.assertEqual(self.a.searchMatrix([
                                              [1,   3,  5,  7],
                                              [10, 11, 16, 20],
                                              [23, 30, 34, 50]
                                            ],4),False)


if __name__ == '__main__':
    unittest.main()
