# encoding: utf8
'''
Multiply Strings
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.

高精度乘法。模拟手乘即可。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        l1=len(num1)
        l2=len(num2)
        l3=l1+l2
        num1=num1[::-1]
        num2=num2[::-1]
        ans=[0 for i in range(l3)]
        for i in range(l1):
            for j in range(l2):
                tmp        =ans[i+j]+int(num1[i])*int(num2[j])
                ans[i+j+1]+=tmp/10
                ans[i+j]   =tmp%10
        ans=ans[::-1]
        # print ans
        for i in range(l3):
            if ans[i]!=0:
                break
        ans=ans[i:]
        ss=map(lambda x:str(x),ans)
        return "".join(ss)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.multiply("123","1"),"123")
        self.assertEqual(self.a.multiply("123","10"),"1230")
        self.assertEqual(self.a.multiply("123","100"),"12300")
        self.assertEqual(self.a.multiply("123","00100"),"12300")
        self.assertEqual(self.a.multiply("123","123"),"15129")

if __name__ == '__main__':
    unittest.main()


