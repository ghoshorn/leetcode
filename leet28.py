'''
Implement strStr()
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

要注意特殊情况，比如strstr("","") 应该等于0 =_=
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        l1=len(haystack)
        l2=len(needle)
        if l2==0:
            return 0
        for i in range(l1-l2+1):
            for j in range(l2):
                if haystack[i+j]!=needle[j]:
                    break
                if j==l2-1:
                    return i
        return -1

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.strStr("abcdefg","cd"),2)
        self.assertEqual(self.a.strStr("abcde","gg"),-1)
        self.assertEqual(self.a.strStr("",""),0)
        self.assertEqual(self.a.strStr("a","a"),0)
        self.assertEqual(self.a.strStr("mississippi", "issip"),4)

if __name__ == '__main__':
    unittest.main()