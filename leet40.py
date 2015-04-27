# encoding: utf8
'''
Combination Sum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 

类似leetcode 39 Combination Sum，只是同一个数不能用多次。直接DFS即可。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        self.nums=sorted(candidates)
        self.l=len(candidates)
        self.ans=[]
        self.dfs(0,[],target)
        # pprint(self.ans)
        return self.ans

    def dfs(self, k, s, target):
        if target==0:
            if s not in self.ans:
                self.ans.append(s)
            # print s
            return
        if k>=self.l:
            return
        if self.nums[k]<=target:
            self.dfs(k+1,s+[self.nums[k]],target-self.nums[k])
        if k+1<self.l and self.nums[k+1]<=target:
            self.dfs(k+1,s,target)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.combinationSum2([10,1,2,7,6,1,5],8),[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])


if __name__ == '__main__':
    unittest.main()


