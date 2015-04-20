import unittest
from pprint import pprint
import pdb

class Solution:
    # @return an integer
    def reverse(self, x):
        tmp=abs(x)
        if tmp!=x:
            flag=1
        else:
            flag=0
        xx=0
        while tmp>0:
            xx=xx*10+tmp%10
            tmp=tmp/10
        if flag:
            xx=-xx
        # print x,xx
        if xx>2147483647 or xx<-2147483648:
            xx=0
        return xx

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.reverse(123),321)
        self.assertEqual(self.a.reverse(-123),-321)
        self.assertEqual(self.a.reverse(0),0)
        self.assertEqual(self.a.reverse(1000000003),0)
        self.assertEqual(self.a.reverse(1534236469),0)

if __name__ == '__main__':
    unittest.main()