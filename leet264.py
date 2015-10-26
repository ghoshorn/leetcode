# encoding: utf8
'''
Ugly Number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).


https://leetcode.com/discuss/52905/my-16ms-c-dp-solution-with-short-explanation
We have an array k of first n ugly number. We only know, at the beginning, the first one, 
which is 1. Then

k[1] = min( k[0]x2, k[0]x3, k[0]x5). The answer is k[0]x2. So we move 2's pointer to 1. 
Then we test:

k[2] = min( k[1]x2, k[0]x3, k[0]x5). And so on. Be careful about the cases such as 6, 
in which we need to forward both pointers of 2 and 3.
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[1]
        p2=p3=p5=0
        for i in xrange(1,n):
            k=min(ans[p2]*2,ans[p3]*3,ans[p5]*5)
            if k==ans[p2]*2:
                p2+=1
            if k==ans[p3]*3:
                p3+=1
            if k==ans[p5]*5:
                p5+=1
            ans.append(k)
        return ans[-1]

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.nthUglyNumber(1),1)
        self.assertEqual(self.a.nthUglyNumber(4),4)
        self.assertEqual(self.a.nthUglyNumber(10),12)

if __name__ == '__main__':
    unittest.main()