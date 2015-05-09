# encoding: utf8
'''
Unique Paths II
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
eg. 3*7
1 1 1
1 0 1
1 1 2

和Unique Paths类似，有障碍的地方设为0即可。
特殊：初始化的时候，遇到障碍之后，之后的点都不再置为1.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        matrix=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==0:
                matrix[i][0]=1
            else:
                break
        for i in range(n):
            if obstacleGrid[0][i]==0:
                matrix[0][i]=1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
                else:
                    matrix[i][j]=0
        # pprint(matrix)
        return matrix[m-1][n-1]


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]),2)
        self.assertEqual(self.a.uniquePathsWithObstacles([[1,0]]),0)
        

if __name__ == '__main__':
    unittest.main()
