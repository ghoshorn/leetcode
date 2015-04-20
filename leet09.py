'''
Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

原来负数不是回文的。。
'''

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