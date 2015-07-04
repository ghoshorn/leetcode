# encoding: utf8
'''
Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
基数里没有0的26进制。。比较坑
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ret=''
        while n>0:
            n-=1
            ret=s[n%26]+ret
            n=n/26
        return ret

# 错误！ 比如26*2=52
# 按此方法，会生成B0，但是个位不能是0！
# 虽然说是26进制，但是没有0的存在。。
class Solution1:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        s='ZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ret=''
        while n>0:
            ret=s[n%26]+ret
            if n<=26:
                break
            n=n/26
        return ret


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.convertToTitle(1), 'A')
        self.assertEqual(self.a.convertToTitle(2), 'B')
        self.assertEqual(self.a.convertToTitle(26), 'Z')
        self.assertEqual(self.a.convertToTitle(27), 'AA')
        self.assertEqual(self.a.convertToTitle(28), 'AB')
        self.assertEqual(self.a.convertToTitle(52), 'AZ')
        self.assertEqual(self.a.convertToTitle(702), 'AAZ')


if __name__ == '__main__':
    unittest.main()