# encoding: utf8
'''
Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

DFS，再用leetcode 36 Valid Sudoku检验即可。
注意：Python里，不要board[i][j]=str(k)，字符串是不可变对象。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        a=[]
        for i in range(9):
            tmp=[]
            for j in range(9):
                if board[i][j]=='.':
                    tmp.append(0)
                else:
                    tmp.append(int(board[i][j]))
            a.append(tmp)
        self.dfs(a,0,0)

    def dfs(self, board,x,y):
        if self.isValidSudoku(board)==False:
            return
        # print "-------------"
        # pprint(board)
        # print x,y
        if x==9 and y==0:
            pprint(board)
            return
        if board[x][y]==0:
            for k in range(1,10):
                # print "x:%d,y:%d  k->%d"%(x,y,k)
                board[x][y]=k
                if y==8:
                    self.dfs(board,x+1,0)
                else:
                    self.dfs(board,x,y+1)
                board[x][y]=0
        else:
            if y==8:
                self.dfs(board,x+1,0)
            else:
                self.dfs(board,x,y+1)

    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j]!=0:
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i]!=0:
                    if board[j][i] in s:
                        return False
                    else:
                        s.add(board[j][i])
        rectlist=[[0,0],[0,3],[0,6],
                [3,0],[3,3],[3,6],
                [6,0],[6,3],[6,6]]
        i=0
        for x,y in rectlist:
            s=set()
            if board[x][y]!=0:
                if board[x][y] in s:
                    return False
                else:
                    s.add(board[x][y])
            if board[x][y+1]!=0:
                if board[x][y+1] in s:
                    return False
                else:
                    s.add(board[x][y+1])
            if board[x][y+2]!=0:
                if board[x][y+2] in s:
                    return False
                else:
                    s.add(board[x][y+2])
            if board[x+1][y]!=0:
                if board[x+1][y] in s:
                    return False
                else:
                    s.add(board[x+1][y])
            if board[x+1][y+1]!=0:
                if board[x+1][y+1] in s:
                    return False
                else:
                    s.add(board[x+1][y+1])
            if board[x+1][y+2]!=0:
                if board[x+1][y+2] in s:
                    return False
                else:
                    s.add(board[x+1][y+2])
            if board[x+2][y]!=0:
                if board[x+2][y] in s:
                    return False
                else:
                    s.add(board[x+2][y])
            if board[x+2][y+1]!=0:
                if board[x+2][y+1] in s:
                    return False
                else:
                    s.add(board[x+2][y+1])
            if board[x+2][y+2]!=0:
                if board[x+2][y+2] in s:
                    return False
                else:
                    s.add(board[x+2][y+2])
        return True

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.solveSudoku(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]),True)



if __name__ == '__main__':
    # unittest.main()
    a=Solution()
    a.solveSudoku(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"])
