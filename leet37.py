# encoding: utf8
'''
Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

DFS，再用leetcode 36 Valid Sudoku检验即可。
注意：Python里，不要board[i][j]=str(k)，字符串是不可变对象。

考虑先转换为二维数组（列表），找到答案后再转换回字符串。

超时后，考虑剪枝优化：
判断是否valid的时候，传入当前变化的坐标xx，yy
1 判断行时，xx行之前的就不需要判断了
2 判断列时，yy列之前的不需要判断
3 判断九宫格时，不在当前坐标范围内的九宫格同意不必判断
剪枝后AC.
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
        # pprint(self.aa)
        for i in range(9):
            board[i]=""
            for j in range(9):
                board[i]+=str(self.aa[i][j])
        # print(board)

    def dfs(self, board,x,y):
        # print "-------------"
        # pprint(board)
        # print x,y
        if x==9 and y==0:
            # pprint(board)
            from copy import deepcopy
            self.aa=deepcopy(board)
            return 1
        if board[x][y]==0:
            for k in range(1,10):
                # print "x:%d,y:%d  k->%d"%(x,y,k)
                board[x][y]=k
                if self.isValidSudoku(board,x,y):
                    if y==8:
                        ret=self.dfs(board,x+1,0) 
                    else:
                        ret=self.dfs(board,x,y+1)
                    if ret:
                        return 1
                board[x][y]=0
        else:
            if y==8:
                ret=self.dfs(board,x+1,0)
            else:
                ret=self.dfs(board,x,y+1)
            if ret:
                return 1

    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board,xx,yy):
        for i in range(xx,9):
            s={}
            for j in range(9):
                if board[i][j]!=0:
                    if board[i][j] in s:
                        return False
                    else:
                        s[board[i][j]]=1
        for i in range(yy,9):
            s={}
            for j in range(9):
                if board[j][i]!=0:
                    if board[j][i] in s:
                        return False
                    else:
                        s[board[j][i]]=1
        rectlist=[[0,0],[0,3],[0,6],
                [3,0],[3,3],[3,6],
                [6,0],[6,3],[6,6]]
        for x,y in rectlist:
            if xx>=x+3 or yy>=y+3 or xx<x or yy<y:
                continue
            s={}
            if board[x][y]!=0:
                if board[x][y] in s:
                    return False
                else:
                    s[board[x][y]]=1
            if board[x][y+1]!=0:
                if board[x][y+1] in s:
                    return False
                else:
                    s[board[x][y+1]]=1
            if board[x][y+2]!=0:
                if board[x][y+2] in s:
                    return False
                else:
                    s[board[x][y+2]]=1
            if board[x+1][y]!=0:
                if board[x+1][y] in s:
                    return False
                else:
                    s[board[x+1][y]]=1
            if board[x+1][y+1]!=0:
                if board[x+1][y+1] in s:
                    return False
                else:
                    s[board[x+1][y+1]]=1
            if board[x+1][y+2]!=0:
                if board[x+1][y+2] in s:
                    return False
                else:
                    s[board[x+1][y+2]]=1
            if board[x+2][y]!=0:
                if board[x+2][y] in s:
                    return False
                else:
                    s[board[x+2][y]]=1
            if board[x+2][y+1]!=0:
                if board[x+2][y+1] in s:
                    return False
                else:
                    s[board[x+2][y+1]]=1
            if board[x+2][y+2]!=0:
                if board[x+2][y+2] in s:
                    return False
                else:
                    s[board[x+2][y+2]]=1
        return True

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        xx=["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
        self.a.solveSudoku(xx)
        self.assertEqual(xx,['534678912', '672195348', '198342567', '859761423', '426853791', '713924856', '961537284', '287419635', '345286179'])
        
        xx=[".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]
        self.a.solveSudoku(xx)
        self.assertEqual(xx,['312547869', '947681235', '658932714', '185364972', '293718456', '476295381', '864123597', '729856143', '531479628'])

if __name__ == '__main__':
    unittest.main()
    # a=Solution()
    # xx=["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
    # a.solveSudoku(xx)
    # pprint(xx)

