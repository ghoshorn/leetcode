# encoding: utf8
'''
Spiral Matrix II 
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

思路和leetcode 54 Spiral Matrix一样。
从[0,0]开始向右走，越界或者遍历过就转向下；以此类推。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    right =0
    down  =1
    left  =2
    up    =3
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        self.n      =n
        if self.n==0:
            return []
        self.matrix  =[[0 for i in range(self.n)] for j in range(self.n)] #是否走过
        self.go(0,0,self.right,1)
        for line in self.matrix:
            for x in line:
                print x,' ',
            print 
        return self.matrix

    # @x,@y this point
    # @direction, 0:right; 1:down; 2:left; 3:up
    # @k put k in position [x,y]
    def go(self, x, y, direction,k):
        if k>self.n*self.n:
            return
        self.matrix[x][y]=k
        if direction==self.right:
            if y+1<self.n and self.matrix[x][y+1]==0:
                self.go(x,y+1,direction,k+1)
            else:
                self.go(x+1,y,direction+1,k+1)
        elif direction==self.down:
            if x+1<self.n and self.matrix[x+1][y]==0:
                self.go(x+1,y,direction,k+1)
            else:
                self.go(x,y-1,direction+1,k+1)
        elif direction==self.left:
            if y>0 and self.matrix[x][y-1]==0:
                self.go(x,y-1,direction,k+1)
            else:
                self.go(x-1,y,direction+1,k+1)
        elif direction==self.up:
            if x>0 and self.matrix[x-1][y]==0:
                self.go(x-1,y,direction,k+1)
            else:
                self.go(x,y+1,(direction+1)%4,k+1)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        sq=[
             [ 1, 2, 3 ],
             [ 8, 9, 4 ],
             [ 7, 6, 5 ]
            ]
        self.assertEqual(self.a.generateMatrix(3),sq)
        self.assertEqual(self.a.generateMatrix(0),[])
        self.assertEqual(self.a.generateMatrix(1),[[1]])

if __name__ == '__main__':
    unittest.main()
