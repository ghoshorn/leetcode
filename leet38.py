# encoding: utf8
'''
Count and Say
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

从头到尾统计连续数字的个数即可。字符串最后加个特殊字符方便处理，避免越界判断。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        from copy import deepcopy
        s='1.'
        for t in range(1,n):
            l=len(s)-1
            tmp=""
            i=0
            while i<l:
                now=s[i]
                times=0
                while s[i]==now:
                    times+=1
                    i+=1
                tmp=tmp+str(times)+str(now)
            tmp=tmp+"."
            s=deepcopy(tmp)
        return s[:-1]
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.countAndSay(1),'1')
        self.assertEqual(self.a.countAndSay(2),'11')
        self.assertEqual(self.a.countAndSay(3),'21')
        self.assertEqual(self.a.countAndSay(4),'1211')
        self.assertEqual(self.a.countAndSay(5),'111221')

if __name__ == '__main__':
    unittest.main()


