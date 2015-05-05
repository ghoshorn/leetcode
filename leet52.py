# encoding: utf8
'''
N-Queens II
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        self.nn=n
        # self.row={}
        self.column={}
        self.xie1={}
        self.xie2={}
        self.ans=0
        self.map=[['.' for i in range(n)] for j in range(n)]
        self.dfs(0)
        return self.ans

    # @k placing the k-th Queen
    def dfs(self,k):
        if k==self.nn:
            self.ans+=1
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
        self.assertEqual(self.a.totalNQueens(4),2)


if __name__ == '__main__':
    unittest.main()
