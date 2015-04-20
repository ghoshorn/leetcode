import unittest
from pprint import pprint
import pdb

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        s=str(x)
        i2=len(s)-1
        i1=0
        while i1<=i2:
            if s[i1]!=s[i2]:
                return False
            i1+=1
            i2-=1
        return True


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isPalindrome(123),False)
        self.assertEqual(self.a.isPalindrome(-12321),False)
        self.assertEqual(self.a.isPalindrome(+12321),True)
        self.assertEqual(self.a.isPalindrome(-2147447412),False)


if __name__ == '__main__':
    unittest.main()