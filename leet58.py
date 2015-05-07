# encoding: utf8
'''
Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
'''

import unittest
from pprint import pprint
import pdb


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if len(s.strip())==0:
            return 0
        l=0
        for x in s.strip()[::-1]:
            if x==' ':
                return l
            else:
                l+=1
        return l

class testCase(unittest.TestCase):
    def setUp(self):
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.lengthOfLastWord("Hello World"),5)
        self.assertEqual(self.a.lengthOfLastWord("World"),5)
        self.assertEqual(self.a.lengthOfLastWord("  "),0)
        self.assertEqual(self.a.lengthOfLastWord("a "),1)


if __name__ == '__main__':
    unittest.main()
