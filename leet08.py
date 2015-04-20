# encoding: utf8
'''
String to Integer (atoi)
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @return an integer
    def atoi(self, str):
        str=str.strip()
        if str=='':
            return 0
        start=flag=0
        num=0
        l=len(str)
        if str[0]=='-':
            flag=1
            start=1
        elif str[0]=='+':
            start=1
        for i in range(start,l):
            if '0'<=str[i]<='9':
                num=num*10+int(str[i])
            else:
                break
                # return 0
        if flag:
            num=-num
        if num>2147483647:
            num=2147483647
        if num<-2147483648:
            num=-2147483648
        return num


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.atoi('+123'),123)
        self.assertEqual(self.a.atoi('123'),123)
        self.assertEqual(self.a.atoi(''),0)
        self.assertEqual(self.a.atoi('-0012a42'),-12)
        self.assertEqual(self.a.atoi('-123'),-123)
        self.assertEqual(self.a.atoi('0'),0)
        self.assertEqual(self.a.atoi('1000000003'),1000000003)
        self.assertEqual(self.a.atoi('000000003'),3)
        self.assertEqual(self.a.atoi('1534236469'),1534236469)

if __name__ == '__main__':
    unittest.main()