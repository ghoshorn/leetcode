# encoding: utf8
'''
Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

先遍历一遍，把包含0的行号和列号记录下来，第二次遍历的时候，如果行号或列号被记录过，就设为0. uses O(m + n) space

改进。第一次遍历，把包含0的行的首行对应位置置零，列的首列对应位置置零。节省了O(m+n)的空间。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row={}
        colomn={}
        l1=len(matrix)
        if l1>0:
            l2=len(matrix[0])
        for i in range(l1):
            for j in range(l2):
                if matrix[i][j]==0:
                    row[i]=1
                    colomn[j]=1
        for i in range(l1):
            for j in range(l2):
                if i in row or j in colomn:
                    matrix[i][j]=0
        pprint(matrix)
        return None

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.setZeroes([[1,0,0],[0,1,1]]),None)


if __name__ == '__main__':
    unittest.main()
