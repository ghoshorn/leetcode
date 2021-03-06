# encoding: utf8
'''
Number of Digit One
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.

Solution on https://leetcode.com/discuss/44281/4-lines-o-log-n-c-java-python

Go through the digit positions by using position multiplier m with values 1, 10, 100, 1000, etc.

For each position, split the decimal representation into two parts, for example 
split n=3141592 into a=31415 and b=92 when we're at m=100 for analyzing the hundreds-digit. 
And then we know that the hundreds-digit of n is 1 for prefixes "" to "3141", i.e., 3142 times. 
Each of those times is a streak, though. Because it's the hundreds-digit, each streak is 100 long. So (a / 10 + 1) * 100 times, the hundreds-digit is 1.

Consider the thousands-digit, i.e., when m=1000. Then a=3141 and b=592. The thousands-digit 
is 1 for prefixes "" to "314", so 315 times. And each time is a streak of 1000 numbers. 
However, since the thousands-digit is a 1, the very last streak isn't 1000 numbers but 
only 593 numbers, for the suffixes "000" to "592". So (a / 10 * 1000) + (b + 1) times, 
the thousands-digit is 1.

The case distincton between the current digit/position being 0, 1 and >=2 can easily be done 
in one expression. With (a + 8) / 10 you get the number of full streaks, and a % 10 == 1 tells 
you whether to add a partial streak.
'''

import unittest
from pprint import pprint
import pdb

class Solution: # easier to understand
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        ones, m = 0, 1
        while m <= n:
            a=n/m
            b=n%m
            if a % 10<=1:
                ones += a/10*m+b+1
            else:
                ones += (a/10+1)*m
            m *= 10
        return ones

class Solution2: # good
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n%m + 1)
            m *= 10
        return ones

class Solution1: # wrong, only get the most position 1
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        nn=str(n)
        ans=0
        while len(nn)>0:
            while nn[0]=='0': # remove useless zero in the front
                nn=nn[1:]
            if nn=='0':
                break
            elif len(nn)==1:
                ans+=1
                break
            nn=nn[1:]
            if nn=='':
                break
            else:
                ans+=int(nn)+1
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.countDigitOne(13), 6)


if __name__ == '__main__':
    unittest.main()