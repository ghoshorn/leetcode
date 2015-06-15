# encoding: utf8
'''
Pascal's Triangle II
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        ans1=[1]
        for i in range(2,rowIndex+2):
            ans2=[1]
            for j in range(2,i):
                ans2.append(ans1[j-2]+ans1[j-1])
            ans2.append(1)
            ans1=ans2
        return ans1

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        x=self.a.getRow(1)
        pprint(x)

if __name__ == '__main__':
    unittest.main()