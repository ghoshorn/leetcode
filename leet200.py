# encoding: utf8
'''
Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

直接Floodfill.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        cnt=0
        l1=len(grid)
        if l1==0:
            return 0
        l2=len(grid[0])
        self.l1=l1
        self.l2=l2
        self.grid=[[] for i in range(l1)]
        for i in range(l1):
            for j in range(l2):
                self.grid[i].append(grid[i][j])
        for i in range(l1):
            for j in range(l2):
                if self.grid[i][j]=='1':
                    cnt+=1
                    self.floodfill(i,j)
        return cnt

    def floodfill(self, x, y):
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        self.grid[x][y]='0'
        for d in direction:
            xx=x+d[0]
            yy=y+d[1]
            if xx>=0 and yy>=0 and xx<self.l1 and yy<self.l2 and self.grid[xx][yy]=='1':
                self.floodfill(xx,yy)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=['1']
        self.assertEqual(self.a.numIslands(a), 1)

        a=["1011011"]
        self.assertEqual(self.a.numIslands(a), 3)

        a= ['11110',
            '11010',
            '11000',
            '00000']
        self.assertEqual(self.a.numIslands(a), 1)


if __name__ == '__main__':
    unittest.main()