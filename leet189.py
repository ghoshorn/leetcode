# encoding: utf8
'''
Rotate Array
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        l=len(nums)
        if l==0 or l==1:
            return
        k=k%l # in case of (1,2),3
        self.reverse(nums,0,l-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,l-1)

    def reverse(self, nums, start, end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=[1,2,3,4,5,6,7]
        self.a.rotate(a,3)
        self.assertEqual(a, [5,6,7,1,2,3,4])


if __name__ == '__main__':
    unittest.main()