# encoding: utf8
'''
Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

把变换写出来，找规律。
[0,0] [0,1] ... [0,n-1]             [n-1,0] [n-2,0] ... [0,0]
[1,0] [1,2] ... [1,n-1]             [n-1,1] [n-2,1] ... [0,1]
...                 ...     --->    ...
[n-2,0] ...     [n-2,n-1]           [n-2,n-2] ...       
[n-1,0] ...     [n-1,n-1]           [n-1,n-1] [n-2,n-1] .[0,n-1]
只看对应4个点，如[0,1]
[0,1]     => [1,n-1]
[1,n-1]   => [n-1,n-2]
[n-1,n-2] => [n-2,0]
[n-2,0]   => [0,1] 
更一般的，对于[x,y]
[x,y]         => [y,n-1-x]
[y,n-1-x]     => [n-1-x,n-1-y]
[n-1-x,n-1-y] => [n-1-y,x]
[n-1-y,x]     => [x,y]
即对于[x1,y1]->[x2,y2]，有y1=x2,x1+y2=n-1。

据此，只需要循环matrix的左上矩阵即可。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n=len(matrix)
        for x in range((n+1)/2):
            for y in range(n/2):
                matrix[x][y],matrix[y][n-1-x],matrix[n-1-x][n-1-y],matrix[n-1-y][x]=\
                matrix[n-1-y][x],matrix[x][y],matrix[y][n-1-x],matrix[n-1-x][n-1-y]
                # print x,y
                # for i in matrix:
                #     print(i)
                # print("--")


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        x=[[1,2,3],[4,5,6],[7,8,9]]
        for i in x:
            print(i)
        print("------")
        self.assertEqual(self.a.rotate(x),None)
        for i in x:
            print(i)
        x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        for i in x:
            print(i)
        print("------")
        self.assertEqual(self.a.rotate(x),None)
        for i in x:
            print(i)



if __name__ == '__main__':
    unittest.main()


