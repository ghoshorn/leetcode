# encoding: utf8
'''
Plus One
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

注意的情况：如果加1后多一位！
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        l=len(digits)
        digits[l-1]+=1
        for i in range(l-1,0,-1):
            if digits[i]>9:
                digits[i]-=10
                digits[i-1]+=1
        if digits[0]>9:
            digits[0]-=10
            digits.insert(0,1)
        return digits


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.plusOne([1,2,3]),[1,2,4])
        self.assertEqual(self.a.plusOne([1,2,9]),[1,3,0])
        self.assertEqual(self.a.plusOne([9]),[1,0])
        

if __name__ == '__main__':
    unittest.main()
