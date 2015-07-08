# encoding: utf8
'''
Contains Duplicate II 
Given an array of integers and an integer k, find out whether there there 
are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the difference between i and j is at most k.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dic={}
        for i in range(len(nums)):
            x=nums[i]
            if x in dic:
                if i-dic[x]<=k:
                    return True
            dic[x]=i
        return False


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.containsNearbyDuplicate([], 0), False)

if __name__ == '__main__':
    unittest.main()