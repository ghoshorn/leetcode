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