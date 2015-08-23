# encoding: utf8
'''
Add Digits 
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods?
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.
https://en.wikipedia.org/wiki/Digital_root
'''

import unittest
from pprint import pprint
import pdb

class Solution1(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            tmp=0
            while num>0:
                tmp+=num%10
                num/=10
            num=tmp
        return num

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        num=num%9
        if num==0:
            return 9
        else:
            return num

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.addDigits(38), 2)

if __name__ == '__main__':
    unittest.main()
    a=Solution()
    for i in range(30):
        print i,' ',a.addDigits(i),' ',i%9