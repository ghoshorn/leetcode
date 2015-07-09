# encoding: utf8
'''
Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

设f[i][j]表示矩阵[i][j]位置的矩阵的最大边长（以[i][j]为右下角）。
f[i][j]=f[i-1][j-1]+1, 如果[i][j]位置的上面和左边f[i-1][j-1]个都是1；
f[i][j]=min([i][j]位置上面连续1的个数，左边连续1的个数)+1
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        l1=len(matrix)
        if l1==0:
            return 0
        self.matrix =matrix
        l2          =len(matrix[0])
        f           =[[0 for i in range(l2)] for j in range(l1)]
        maxlen      =0
        for i in range(l2):
            if matrix[0][i]=='1':
                f[0][i]=1
                maxlen=1
        for i in range(l1):
            if matrix[i][0]=='1':
                f[i][0]=1
                maxlen=1
        for i in range(1,l1):
            for j in range(1,l2):
                if matrix[i][j]=='1':
                    up1   =self.up1(i,j)
                    left1 =self.left1(i,j)
                    if up1>=f[i-1][j-1] and left1>=f[i-1][j-1]:
                        f[i][j]=f[i-1][j-1]+1
                    else:
                        f[i][j]=min(up1,left1)+1
                    maxlen=max(maxlen,f[i][j])
        # for x in f:
        #     print x
        return maxlen*maxlen

    def up1(self, x, y):
        cnt=0
        while x>0:
            x-=1
            if self.matrix[x][y]=='0':
                return cnt
            cnt+=1
        return cnt

    def left1(self, x, y):
        cnt=0
        while y>0:
            y-=1
            if self.matrix[x][y]=='0':
                return cnt
            cnt+=1
        return cnt

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=['10100',
            '10111',
            '11111',
            '10010',]
        self.assertEqual(self.a.maximalSquare(a), 4)
        self.assertEqual(self.a.maximalSquare(["1"]), 1)
        a=["0001",
            "1101",
            "1111",
            "0111",
            "0111"]
        self.assertEqual(self.a.maximalSquare(a), 9)

if __name__ == '__main__':
    unittest.main()