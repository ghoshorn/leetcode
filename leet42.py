# encoding: utf8
'''
Trapping Rain Water 
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
图参考http://www.leetcode.com/wp-content/uploads/2012/08/rainwatertrap.png

'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        l=len(height)
        if l==0 or l==1:
            return 0
        maxtoend={}
        maxtoend[l-1]=height[l-1]
        for i in range(l-2,-1,-1):
            maxtoend[i]=max(height[i],maxtoend[i+1]) #此位置到最后，最高的bar的高度
        # print(maxtoend)
        last=0 #前一次bar+水的体积
        vol_all=0 #所有体积（水+bar）
        vol_bar=sum(height) #bar所占的体积
        for i in range(l):
            x=height[i]
            if x<last:
                if last<=maxtoend[i]:
                    vol_all+=last
                elif x<=maxtoend[i]:
                    vol_all+=maxtoend[i]
                    last=maxtoend[i]
            else:
                if x<=maxtoend[i]:
                    last=x
                    vol_all+=x
                else:
                    last=maxtoend[i]
                    vol_all+=maxtoend[i]
            # print i,vol_all
        return vol_all-vol_bar
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.trap([0,1,0,2,1,0,1,3,2,1,2,1]),6)
        self.assertEqual(self.a.trap([4,2,3]),1)

if __name__ == '__main__':
    unittest.main()


