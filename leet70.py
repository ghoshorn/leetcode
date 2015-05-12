# encoding: utf8
'''
Climbing Stairs
ou are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

斐波那契数列
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        a=1
        b=1
        while n:
            a,b=b,a+b
            n-=1
        return a


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.climbStairs(1),1)
        self.assertEqual(self.a.climbStairs(2),2)
        self.assertEqual(self.a.climbStairs(3),3)


if __name__ == '__main__':
    unittest.main()
