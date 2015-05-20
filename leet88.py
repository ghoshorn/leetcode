# encoding: utf8
'''
Merge Sorted Array  
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold 
additional elements from nums2. The number of elements initialized in nums1 and nums2 are 
m and n respectively.

nums1中有多余元素，不可直接append.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        i=j=0
        if n==0:
            return None
        nums1[m:]=[]
        # if m==0:
            # from copy import deepcopy
            # nums1=deepcopy(nums2)
            # print nums1
            # nums1=nums2
            # return None
        while i<m and j<n:
            if nums2[j]<nums1[i]:
                nums1.insert(i,nums2[j])
                m+=1
                j+=1
                i+=1
            else:
                i+=1
        while j<n:
            nums1.append(nums2[j])
            j+=1
        return None


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=[1,3,5,6,8]
        b=[2,4,7,9]
        self.a.merge(a,len(a),b,len(b))
        print a
        self.assertEqual(a,[1,2,3,4,5,6,7,8,9])

        a=[0]
        self.a.merge(a, 0, [1], 1)
        print a
        self.assertEqual(a,[1])

        a=[1,0]
        self.a.merge(a, 1, [2], 1)
        print a
        self.assertEqual(a,[1,2])

        a=[4,5,6,0,0,0]
        self.a.merge(a, 3, [1,2,3], 3)
        print a
        self.assertEqual(a,[1,2,3,4,5,6])


if __name__ == '__main__':
    unittest.main()