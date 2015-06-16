# encoding: utf8
'''
Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        l=len(s)
        if l==0 or l==1:
            return True
        i=0
        j=l-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if i>=j:
                break
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isPalindrome("A man, a plan, a canal: Panama"),True)
        self.assertEqual(self.a.isPalindrome("race a car"),False)
        self.assertEqual(self.a.isPalindrome(",."),True)

if __name__ == '__main__':
    unittest.main()