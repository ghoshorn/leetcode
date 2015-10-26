# encoding: utf8
'''
Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant extra space complexity?
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        nums.append(None)
        if l==0:
            return 0
        for i in xrange(l):
            while nums[i]!=None and nums[i]!=i:
                tmp=nums[i]
                nums[i]=nums[tmp]
                nums[tmp]=tmp
                # nums[i],nums[nums[i]]=nums[nums[i]],nums[i]
        for i in xrange(l):
            if nums[i]!=i:
                return i
        return l

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.missingNumber([0,1,3]),2)
        self.assertEqual(self.a.missingNumber([0,1,2]),3)
        self.assertEqual(self.a.missingNumber([0,1,2,3,4,6]),5)
        self.assertEqual(self.a.missingNumber([0,1]),2)
        self.assertEqual(self.a.missingNumber([1,0]),2)
        self.assertEqual(self.a.missingNumber([3,2,0]),1)
        self.assertEqual(self.a.missingNumber([1]),0)

if __name__ == '__main__':
    unittest.main()