# encoding: utf8
'''
Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

DP. 方格取数.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        matrix=[[0 for i in range(n)] for j in range(m)]
        matrix[0][0]=grid[0][0]
        for i in range(1,m):
            matrix[i][0]=matrix[i-1][0]+grid[i][0]
        for i in range(1,n):
            matrix[0][i]=matrix[0][i-1]+grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j]=grid[i][j]+min(matrix[i-1][j],matrix[i][j-1])
        # pprint(grid);print;pprint(matrix)
        return matrix[m-1][n-1]


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=[ [1,2,3],
            [2,3,4],
            [1,3,2]]
        self.assertEqual(self.a.minPathSum(a),9)
        

if __name__ == '__main__':
    unittest.main()
