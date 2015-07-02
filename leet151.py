# encoding: utf8
'''
Reverse Words in a String
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

偷懒，直接使用了Python的优雅的一行搞定。

换成c的话，思路是:
1 去除多余的空格，O(n)
2 把整个字符串reverse，O(n)
3 把每个单词reverse,O(n)
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.strip().split()[::-1])

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(self.a.reverseWords("   a   b "), "b a")

if __name__ == '__main__':
    unittest.main()