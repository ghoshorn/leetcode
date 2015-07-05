# encoding: utf8
'''
Excel Sheet Column Number
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        ret=0
        base=1
        for x in s[::-1]:
            xx=ord(x)-ord('A')+1
            ret+=base*xx
            base*=26
        return ret

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.titleToNumber('A'), 1)
        self.assertEqual(self.a.titleToNumber('Z'), 26)
        self.assertEqual(self.a.titleToNumber('AA'), 27)
        self.assertEqual(self.a.titleToNumber("AB"), 28)


if __name__ == '__main__':
    unittest.main()