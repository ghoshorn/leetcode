# encoding: utf8
'''
Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

用last[i]记录最后i个中最大是多少；
从头开始计算当前值与从当前开始到最后的最大值的差额，取最大即可。
O(n).
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        from copy import deepcopy
        last=deepcopy(prices)
        l=len(prices)
        for i in range(l-2,-1,-1):
            if last[i]<last[i+1]:
                last[i]=last[i+1]
        ans=0
        for i in range(l):
            ans=max(ans,last[i]-prices[i])
        return ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        x=[5,3,6,2,4]
        self.assertEqual(self.a.maxProfit(x),3)

if __name__ == '__main__':
    unittest.main()