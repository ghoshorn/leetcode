# encoding: utf8
'''
Valid Sudoku
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

没有填的空项直接忽略，只检验填数的部分，每一行/每一列/每个九宫格没有重复的数字即可。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i]!='.':
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
            if board[x][y]!='.':
                if board[x][y] in s:
                    return False
                else:
                    s.add(board[x][y])
            if board[x][y+1]!='.':
                if board[x][y+1] in s:
                    return False
                else:
                    s.add(board[x][y+1])
            if board[x][y+2]!='.':
                if board[x][y+2] in s:
                    return False
                else:
                    s.add(board[x][y+2])
            if board[x+1][y]!='.':
                if board[x+1][y] in s:
                    return False
                else:
                    s.add(board[x+1][y])
            if board[x+1][y+1]!='.':
                if board[x+1][y+1] in s:
                    return False
                else:
                    s.add(board[x+1][y+1])
            if board[x+1][y+2]!='.':
                if board[x+1][y+2] in s:
                    return False
                else:
                    s.add(board[x+1][y+2])
            if board[x+2][y]!='.':
                if board[x+2][y] in s:
                    return False
                else:
                    s.add(board[x+2][y])
            if board[x+2][y+1]!='.':
                if board[x+2][y+1] in s:
                    return False
                else:
                    s.add(board[x+2][y+1])
            if board[x+2][y+2]!='.':
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
        self.assertEqual(self.a.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]),True)



if __name__ == '__main__':
    unittest.main()
