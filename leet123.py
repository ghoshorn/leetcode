# encoding: utf8
'''
Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).

首先想到的思路是，根据II的算法，得到多次不同的利润，然后排序取最大的两个利润相加，
但是某些情况下错误，比如1,4,2,8,0,4; 

可以根据I的算法，设f[i]为前i天的一次交易最大利润，g[i]为后i天一次交易最大利润，则
ans=max(f[i]+g[i])
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        pre= self.maxProfitPre(prices) # 第i天买入到最后一天可以得到的最大利润
        post= self.maxProfitPost(prices) # 第i天卖出可以得到的最大利润
        l=len(prices)
        for i in range(1,l):
            if post[i]<post[i-1]:
                post[i]=post[i-1] # 前i天买入到最后一天可以得到的最大利润
        for i in range(l-2,-1,-1):
            if pre[i]<pre[i+1]:
                pre[i]=pre[i+1] # 前i天卖出可以得到的最大利润
        # print 'pre  ',pre
        # print 'post ',post
        ans=0
        for x,y in zip(pre,post):
            ans=max(ans,x+y)
        return ans

    def maxProfitPre(self, prices):
        from copy import deepcopy
        last=deepcopy(prices)
        l=len(prices)
        for i in range(l-2,-1,-1):
            if last[i]<last[i+1]:
                last[i]=last[i+1]
        ans=[]
        for i in range(l):
            ans.append(last[i]-prices[i])
        return ans

    def maxProfitPost(self, prices):
        from copy import deepcopy
        first=deepcopy(prices)
        l=len(prices)
        for i in range(1,l):
            if first[i]>first[i-1]:
                first[i]=first[i-1]
        ans=[]
        # print first
        # print prices
        for i in range(l):
            ans.append(prices[i]-first[i])
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        x=[1,3,2,6,5,0,3]
        self.assertEqual(self.a.maxProfit(x),8)

if __name__ == '__main__':
    unittest.main()