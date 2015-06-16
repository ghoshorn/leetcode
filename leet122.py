# encoding: utf8
'''
Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as 
you like (ie, buy one and sell one share of the stock multiple times). However, you may 
not engage in multiple transactions at the same time (ie, you must sell the stock before 
you buy again).
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        ans=0
        l=len(prices)
        if l==0 or l==1:
            return 0
        pricein=-1
        priceout=0
        # 找到第一次买入的价格
        for i in xrange(l-1):
            if prices[i]<prices[i+1]:
                pricein=prices[i]
                break
        i+=1
        while i<l-1:
            # 当前价格比买入高，且下一个价格比当前低，则卖出
            if prices[i]>pricein and prices[i]>prices[i+1]:
                priceout=prices[i]
                ans=ans+(priceout-pricein)
                pricein=prices[i+1]
                i=i+2
            else:
                # 如果当前价格比买入价格低，说明之前不该买入；把买入价格换为当前价格
                if prices[i]<pricein:
                    pricein=prices[i]
                i+=1
        if pricein!=-1 and prices[l-1]>pricein:
            ans=ans+prices[l-1]-pricein
        return ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # x=[5,7,4,8,10]
        # self.assertEqual(self.a.maxProfit(x),8)
        
        # self.assertEqual(self.a.maxProfit([1,2,3,4,5,6,7,8]),7)
        # self.assertEqual(self.a.maxProfit([8,7,6,5,4,3,2,1]),0)
        # self.assertEqual(self.a.maxProfit([1,10]),9)
        # self.assertEqual(self.a.maxProfit([1,1]),0)
        # self.assertEqual(self.a.maxProfit([1]),0)
        # self.assertEqual(self.a.maxProfit([1,4,2]),3)
        # self.assertEqual(self.a.maxProfit([2,1,2,0,1]),2)
        self.assertEqual(self.a.maxProfit([3,2,6,5,0,3]),7)

if __name__ == '__main__':
    unittest.main()