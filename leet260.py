# encoding: utf8
'''
Single Number III 
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

第一遍使用异或，得到只出现一次的两个数的异或值。
第二遍，根据之前的结果(某一位是否为1)，将数分为两组，则必然是 每组中只有一个数出现一次，其他出现两次；
再根据Single Number I的解法，一次异或即可。

在Python中，因为不存在int的关系，需要对正负数分别对待。在C中不需要。

Python中，dif&=-dif,可以不需要区分正负数。为什么？
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dif=0
        for x in nums:
            dif=dif ^ x
        cnt=0
        # print 'dif=',dif
        # while dif>0:
        #     dif=dif>>1
        #     cnt+=1
        # if cnt>1:
        #     dif=1<<(cnt-1)
        # else:
        #     dif=1
        dif&=-dif # bit hack, isolate the rightmost 1-bit
        # print 'dif2=',dif
        n1=0
        n2=0
        for x in nums:
            if x & dif!=0:
                n1=n1^x
            else:
                n2=n2^x
        return [n1,n2]

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.singleNumber([1, 2, 1, 3, 2, 5]),[3,5])
        self.assertEqual(self.a.singleNumber([43772400,1674008457,1779561093,744132272,1674008457,448610617,1779561093,124075538,-1034600064,49040018,612881857,390719949,-359290212,-812493625,124732,-1361696369,49040018,-145417756,-812493625,2078552599,1568689850,865876872,865876872,-1471385435,1816352571,1793963758,2078552599,-1034600064,1475115274,-119634980,124732,661111294,-1813882010,1568689850,448610617,1347212898,-1293494866,612881857,661111294,-1361696369,1816352571,-1813882010,-359290212,1475115274,1793963758,1347212898,43772400,-1471385435,124075538,-1293494866,-119634980,390719949]),[-145417756,744132272])

if __name__ == '__main__':
    unittest.main()