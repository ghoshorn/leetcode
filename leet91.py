# encoding: utf8
'''
Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

需要考虑到0的情况，即0不对应任何字母。
需要考虑的情况比较多。
比如当是2位的时候，如果是00，如果是01，如果是10，如果是26，如果是27，如果是20，都要考虑到。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        l=len(s)
        if l==0:
            return l
        if l==1:
            if int(s)>0:
                return l
            else:
                return 0
        ans=[0 for i in range(l)]
        if s[0]=='0':
            return 0
        else:
            ans[0]=1
        if s.find("00")>=0:
            return 0
        tmp=s[0:2]
        if int(tmp)==0:
            ans[1]=0
        elif int(tmp)<=26 and s[1]!='0':
            ans[1]=2
        elif int(tmp)>26 and s[1]=='0':
            ans[1]=0
        else:
            ans[1]=1
        for i in range(2,l):
            if s[i-1]=='0':
                if 0<int(s[i-2:i])<=26:
                    ans[i]=ans[i-2]
                else:
                    ans[i]=0
            elif s[i]=='0':
                if 0<int(s[i-1:i+1])<=26:
                    ans[i]=ans[i-2]
                else:
                    ans[i]=0
            else:
                tmp=s[i-1:i+1]
                if int(tmp)<=26:
                    ans[i]=ans[i-1]+ans[i-2]
                else:
                    ans[i]=ans[i-1]
        print ans
        return ans[l-1]


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.numDecodings(""),0)
        self.assertEqual(self.a.numDecodings("0"),0)
        self.assertEqual(self.a.numDecodings("12"),2)
        self.assertEqual(self.a.numDecodings("123"),3)
        self.assertEqual(self.a.numDecodings("20"),1)
        self.assertEqual(self.a.numDecodings("00"),0)
        self.assertEqual(self.a.numDecodings("01"),0)
        self.assertEqual(self.a.numDecodings("100"),0)
        self.assertEqual(self.a.numDecodings("110"),1)
        self.assertEqual(self.a.numDecodings("227"),2)
        self.assertEqual(self.a.numDecodings("230"),0)
        self.assertEqual(self.a.numDecodings("30"),0)
        self.assertEqual(self.a.numDecodings("27"),1)


if __name__ == '__main__':
    unittest.main()
