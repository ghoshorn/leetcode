# encoding: utf8
'''
First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

import unittest
from pprint import pprint
import pdb

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        mid=1
        while l<r:
            # mid=(l+r)/2
            mid=l+(r-l)/2 # 这样可以防止溢出
            isbad=isBadVersion(mid)
            if isbad:
                r=mid
            else:
                l=mid+1
        return l

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