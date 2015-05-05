# encoding: utf8
'''
N-Queens 
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.nn=n
        # self.row={}
        self.column={}
        self.xie1={}
        self.xie2={}
        self.ans=[]
        self.map=[['.' for i in range(n)] for j in range(n)]
        self.dfs(0)
        return self.ans

    # @k placing the k-th Queen
    def dfs(self,k):
        if k==self.nn:
            # pprint(self.map)
            # print "+++"
            board=[[] for i in range(self.nn)]
            for i in range(self.nn):
                board[i]=""
                for j in range(self.nn):
                    board[i]+=str(self.map[i][j])
            self.ans.append(board)
            return
        i=k #row
        for j in range(self.nn): # column
            if self.column.get(j,True) and self.xie1.get(i+j,True) and self.xie2.get(i-j,True):
                self.column[j]=False
                self.xie1[i+j]=False
                self.xie2[i-j]=False
                self.map[i][j]='Q'
                self.dfs(k+1)
                self.map[i][j]='.'
                self.column[j]=True
                self.xie1[i+j]=True
                self.xie2[i-j]=True



class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a4=[
             [".Q..",  
              "...Q",
              "Q...",
              "..Q."],

             ["..Q.",  
              "Q...",
              "...Q",
              ".Q.."]
            ]
        self.assertEqual(self.a.solveNQueens(4),a4)


if __name__ == '__main__':
    unittest.main()
