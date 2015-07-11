# encoding: utf8
'''
Summary Ranges 
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if nums==[]:
            return []
        ans=[]
        smallest=nums[0]
        last=nums[0]
        nums.append(-999999)
        l=len(nums)
        for i in xrange(1,l):
            if nums[i]==last+1:
                last=nums[i]
            else:
                if smallest==last:
                    ans.append(str(last))
                else:
                    ans.append('%d->%d'%(smallest,last))
                smallest=last=nums[i]
        return ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.summaryRanges([0,1,2,4,5,7]), ["0->2","4->5","7"])
        self.assertEqual(self.a.summaryRanges([-1]), ["-1"])

if __name__ == '__main__':
    unittest.main()