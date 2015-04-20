# encoding: utf8
'''
Divide Two Integers  
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

Solution1:当divide(-2147483648, -1)，超时。
可以让除数每次翻倍，不够减时每次再折半，运算次数就会在log(MAX_INT)*2=62次之内了。

由于不能使用除法，每次翻倍都要记录翻倍前的数字。
为了应对“If it is overflow, return MAX_INT.”，还需要加上ans与MAX_INT的比较
'''

import unittest
from pprint import pprint
import pdb

class Solution1:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend==0:
            return 0
        ans=0
        a1=abs(dividend)
        a2=abs(divisor)
        while a1>=a2:
            ans+=1
            a1-=a2
        if dividend>0 and divisor>0 or dividend<0 and divisor<0:
            return ans
        else:
            return -ans

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend==0:
            return 0
        ans=0
        a1=abs(dividend)
        a2=[abs(divisor)]
        base=[1]
        p=0
        while a1>=a2[p]:
            ans+=base[p]
            a1-=a2[p]
            a2.append(a2[p]+a2[p])
            base.append(base[p]+base[p])
            p+=1
        while a2[p]>abs(divisor):
            a2.pop()
            p-=1
            while a1>=a2[p]:
                ans+=base[p]
                a1-=a2[p]
        if dividend>0 and divisor>0 or dividend<0 and divisor<0:
            if ans>2147483647:
                return 2147483647
            else:
                return ans
        else:
            if ans>2147483648:
                return -2147483648
            return -ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.divide(2,1),2)
        self.assertEqual(self.a.divide(-2,-1),2)
        self.assertEqual(self.a.divide(-2,1),-2)
        self.assertEqual(self.a.divide(-2147483648, -1),2147483647)


if __name__ == '__main__':
    unittest.main()