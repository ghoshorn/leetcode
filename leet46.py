# encoding: utf8
'''
Permutations
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.ans=[]
        self.l=len(num)
        self.nums=num
        self.b=[True for i in range(self.l)]
        self.dfs([],0)
        # pprint(self.ans)
        return self.ans

    def dfs(self,s,k):
        if k==self.l:
            self.ans.append(s)
            return
        for i in range(self.l):
            if self.b[i]:
                self.b[i]=False
                self.dfs(s+[self.nums[i]],k+1)
                self.b[i]=True

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.permute([1,2,3]),[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2],[3,2,1]])



if __name__ == '__main__':
    unittest.main()


