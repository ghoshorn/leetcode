# encoding: utf8
'''
First Missing Positive
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

从头开始，每次把当前这个数放到它该在的位置。
例如遇到5，则应该有nums[4]=5，如果不是，则交换。
Put each number in its right place.
For example:
When we find 5, then swap it with A[4].
At last, the first place where its number is not right, return the place + 1.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        l=len(nums)
        if l==0:
            return 1
        i=0
        while i<l:
            # if nums[i]!=i+1 and nums[i]-1<l and nums[i]>0:
            if nums[i]-1<l and nums[i]>0 and nums[i]!=nums[nums[i]-1]:
                # print nums
                tmp=nums[i]
                nums[i]=nums[nums[i]-1]
                nums[tmp-1]=tmp
                # swap(nums[i],nums[nums[i]-1])
                # 注意，不要写成下面这种！
                # nums[i],nums[nums[i]-1]=nums[nums[i]-1],nums[i]
            else:
                i+=1
        for i in xrange(l):
            if nums[i]!=i+1:
                return i+1
        return l+1

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.firstMissingPositive([1,2,0]),3)
        self.assertEqual(self.a.firstMissingPositive([3,4,-1,1]),2)
        self.assertEqual(self.a.firstMissingPositive([2]),1)
        self.assertEqual(self.a.firstMissingPositive([1]),2)


if __name__ == '__main__':
    unittest.main()


