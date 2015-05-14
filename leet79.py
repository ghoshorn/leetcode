# encoding: utf8
'''
Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
!!!!!! 实际上应该是 ["ABCE",   (⊙o⊙)
                  "SFCS",
                  "ADEE"]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if word=='':
            return True
        self.word=word
        self.l=len(word)
        self.l1=len(board)
        if self.l1==0:
            return False
        self.l2=len(board[0])
        if self.l2==0:
            return False
        self.matrix=[]
        for i in range(self.l1):
            tmp=[]
            for j in range(self.l2):
                tmp.append(board[i][j])
            self.matrix.append(tmp)
        self.ans=False
        self.directions=[[0,1],[0,-1],[1,0],[-1,0]] # four directions
        for i in range(self.l1):
            for j in range(self.l2):
                if self.matrix[i][j]==word[0]:
                    self.dfs(0,i,j)
        # print(self.ans)
        return self.ans

    def dfs(self, n, x, y):
        if self.matrix[x][y]!=self.word[n]:
            return False
        if n==self.l-1:
            self.ans=True
            return True
        tmp=self.matrix[x][y]
        self.matrix[x][y]='#'
        # pprint(self.matrix)
        # print '---'
        for i in range(4):
            xx=x+self.directions[i][0]
            yy=y+self.directions[i][1]
            if 0<=xx<self.l1 and 0<=yy<self.l2 and self.matrix[xx][yy]!='#':
                ret=self.dfs(n+1, xx, yy)
                if ret:
                    return ret
        self.matrix[x][y]=tmp


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        s=[
          "ABCE",
          "SFCS",
          "ADEE"
        ]
        self.assertEqual(self.a.exist(s,"ABCCED"),True)
        self.assertEqual(self.a.exist(s,"SEE"),True)
        self.assertEqual(self.a.exist(s,"ABCB"),False)
        self.assertEqual(self.a.exist(["a"], "a"),True)
        self.assertEqual(self.a.exist(["aa"], "aa"),True)


if __name__ == '__main__':
    unittest.main()
