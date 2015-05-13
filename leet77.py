# encoding: utf8
'''
Combinations 
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        self.ans=[]
        self.n=n
        self.k=k
        self.valid=[True for i in range(n+1)]
        self.dfs([],1)
        # print(self.ans)
        return self.ans

    def dfs(self, now, k):
        if k==self.k+1:
            self.ans.append(now)
            return
        start=1
        if len(now)>0:
            start=now[-1]
        for i in range(start,self.n+1):
            if self.valid[i]:
                self.valid[i]=False
                self.dfs(now+[i],k+1)
                self.valid[i]=True


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.combine(4,2),[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])


if __name__ == '__main__':
    unittest.main()
