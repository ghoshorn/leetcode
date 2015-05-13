# encoding: utf8
'''
Subsets 
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort() # The solution set must not contain duplicate subsets.
        self.ans=[]
        self.nums=nums
        self.n=len(nums)
        self.valid=[True for i in range(self.n)]
        self.dfs([],0)
        # pprint(self.ans)
        return self.ans

    def dfs(self, now, start):
        if start==self.n+1:
            return
        # if now not in self.ans:
        self.ans.append(now)
        for i in range(start,self.n):
            if self.valid[i]:
                self.valid[i]=False
                self.dfs(now+[self.nums[i]],i+1)
                # self.dfs(now+[self.nums[i]],start+1) #此处不要写错了 ...
                self.valid[i]=True


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.subsets([1,2,3]),[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
        self.assertEqual(self.a.subsets([1,2,3,4,5,6,7,8,10,0]),[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])


if __name__ == '__main__':
    unittest.main()
