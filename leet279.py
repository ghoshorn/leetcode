# encoding: utf8
'''
Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''

import unittest
from pprint import pprint
import pdb
# this is wrong!
class Solution1(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        base=int(math.floor(math.sqrt(n)))
        cnt=0
        while n>0:
            if base*base<=n:
                n=n-base*base
                cnt+=1
            else:
                base-=1
        return cnt

class Solution2(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        f=[65535 for i in xrange(n+1)]
        f[0]=0
        for i in xrange(1,n+1):
            for j in xrange(int(math.sqrt(i))+1):
                f[i]=min(f[i],f[i-j*j]+1)
        return f[n]

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        f=[0]
        while len(f)<=n:
            tmp=65535
            m=len(f)
            for i in xrange(1,int(math.sqrt(m))+1):
                tmp=min(tmp,f[m-i**2]+1)
            f.append(tmp)
        return f[-1]

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.numSquares(12),3)
        self.assertEqual(self.a.numSquares(13),2)

if __name__ == '__main__':
    unittest.main()