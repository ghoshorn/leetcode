# encoding: utf8
'''
H-Index II

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.

根据上题排序的思路，直接二分，则为O(logn)
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        ll=len(citations)
        if ll==0:
            return 0
        # citations.sort()
        l=0
        r=ll-1
        k=0
        while l<=r:
            i=(l+r)/2
            if ll-i<=citations[i]:
                k=ll-i
                r=i-1
            else:
                l=i+1
        return k

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.hIndex([0,1,3,5,6]),3)
        self.assertEqual(self.a.hIndex([0, 0]),0)
        self.assertEqual(self.a.hIndex([0]),0)
        self.assertEqual(self.a.hIndex([0,1]),1)

if __name__ == '__main__':
    unittest.main()