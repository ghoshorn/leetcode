# encoding: utf8
'''
Valid Anagram 
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

每个字母代表一个数字，例如a=1,b=2，如果两个单词的乘积相等，则其包含的字母应该相同。
（需要先判断两个单词是否一样长。）
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        product1=product2=1
        for x in s:
            product1*=(ord(x)-96) # 'a'=97
        for x in t:
            product2*=(ord(x)-96)
        return product1==product2

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isAnagram("anagram", "nagaram"), True)
        self.assertEqual(self.a.isAnagram("rat","car"), False)
        self.assertEqual(self.a.isAnagram("aa","a"), False)

if __name__ == '__main__':
    unittest.main()