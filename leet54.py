# encoding: utf8
'''
Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

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
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        self.n      =len(matrix)
        if self.n==0:
            return []
        self.m      =len(matrix[0])
        self.ans    =[]
        self.matrix =matrix
        self.valid  =[[True for i in range(self.m)] for j in range(self.n)] #是否走过
        self.go(0,0,self.right)
        return self.ans

    # @x,@y this point
    # @direction, 0:right; 1:down; 2:left; 3:up
    def go(self, x, y, direction):
        if len(self.ans)==self.m*self.n:
            return
        self.ans.append(self.matrix[x][y])
        self.valid[x][y]=False
        if direction==self.right:
            if y+1<self.m and self.valid[x][y+1]:
                self.go(x,y+1,direction)
            else:
                self.go(x+1,y,direction+1)
        elif direction==self.down:
            if x+1<self.n and self.valid[x+1][y]:
                self.go(x+1,y,direction)
            else:
                self.go(x,y-1,direction+1)
        elif direction==self.left:
            if y>0 and self.valid[x][y-1]:
                self.go(x,y-1,direction)
            else:
                self.go(x-1,y,direction+1)
        elif direction==self.up:
            if x>0 and self.valid[x-1][y]:
                self.go(x-1,y,direction)
            else:
                self.go(x,y+1,(direction+1)%4)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        sq=[ [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]]
        self.assertEqual(self.a.spiralOrder(sq),[1,2,3,6,9,8,7,4,5])
        self.assertEqual(self.a.spiralOrder([]),[])
        self.assertEqual(self.a.spiralOrder([[2,3]]),[2,3])

if __name__ == '__main__':
    unittest.main()
