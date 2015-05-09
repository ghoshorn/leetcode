# encoding: utf8
'''
Unique Paths 
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        matrix=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,m+1):
            matrix[i][1]=1
        for i in range(1,n+1):
            matrix[1][i]=1
        for i in range(2,m+1):
            for j in range(2,n+1):
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
        # pprint(matrix)
        return matrix[m][n]


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.uniquePaths(3,7),28)
        

if __name__ == '__main__':
    unittest.main()
