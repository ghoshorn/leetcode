# encoding: utf8
'''
Combination Sum
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3]

直接DFS即可。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        self.nums=sorted(candidates)
        self.l=len(candidates)
        self.ans=[]
        self.dfs(0,[],target)
        # pprint(self.ans)
        return self.ans

    def dfs(self, k, s, target):
        if target==0:
            self.ans.append(s)
            # print s
            return
        if self.nums[k]<=target:
            self.dfs(k,s+[self.nums[k]],target-self.nums[k])
        if k+1<self.l and self.nums[k+1]<=target:
            self.dfs(k+1,s,target)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.combinationSum([2,3,6,7],7),[[2,2,3],[7]])
        self.assertEqual(self.a.combinationSum([8,7,4,3], 11),[[3,4,4],[3,8],[4,7]])


if __name__ == '__main__':
    unittest.main()


