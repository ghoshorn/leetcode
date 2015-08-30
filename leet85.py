# encoding: utf8
'''
Maximal Rectangle 
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

height[i][j]=height[i-1][j]+1, if matrix[i][j]==1
height[i][j]=0, if matrix[i][j]==0
例如
00100
01110
11111
则每行的height就是
00100
01210
12321
然后利用leetcode 85 Largest Rectangle in Histogram，每行计算即可。

参考https://leetcode.com/discuss/5198/a-o-n-2-solution-based-on-largest-rectangle-in-histogram
This question is similar as [Largest Rectangle in Histogram]:

You can maintain a row length of Integer array H recorded its height of '1's, and scan and update row by row to find out the largest rectangle of each row.

For each row, if matrix[row][i] == '1'. H[i] +=1, or reset the H[i] to zero. and accroding the algorithm of [Largest Rectangle in Histogram], to update the maximum area.

===============
VS. leetcode 85
Largest Rectangle in Histogram 
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
   # 
  ##
  ##
  ## #
# ####
######
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
   # 
  ++
  ++
  ++ #
# ++##
##++##
The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

思路：
1，直接搜索，大数据超时。
2，对于任一个bar n(下标)，向左找到第一个比它小的记做ln(下标),向右找到第一个比它小的记做rn。则以此bar为高的矩形面积为(rn-ln-1)*height(n)
  对于大数据同样超时。
3，利用2的思路，再利用栈。
    从左至右遍历所有bar，并push到stack里。如果当前的bar高于stack或stack为空，直接push；否则，已栈顶bar为高，根据思路2计算面积。
    此时n=栈顶，ln为弹出n后的栈顶（栈是升序的），rn即为当前bar的下标。面积=(rn-ln-1)*height[n]；如果弹出n后栈为空，则面积=rn*height[n]
    每次计算面积后，保留最大的面积。
    为了方便处理最后一个bar，可在最后插入一个高度为0的bar。
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        max_area=0
        row=len(matrix)
        col=len(matrix[0])
        height=[0 for i in range(col+1)]
        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j]=='1':
                    height[j]+=1
                else:
                    height[j]=0
            max_area=max(max_area, self.largestRectangleArea(height))
        return max_area

    def largestRectangleArea(self, height):
        s=[]
        l=len(height)
        height.insert(l,0)
        l+=1
        ans=height[0]
        i=0
        while i<l:
        # for i in xrange(l):
            if len(s)==0 or height[i]>=height[s[len(s)-1]]:
                s.insert(len(s),i)
                i+=1
            else:
                rn=i
                n=s.pop()
                if len(s)==0:
                    ln=0
                    ans=max(ans,rn*height[n])
                else:
                    ln=s[len(s)-1]
                    ans=max(ans,(rn-ln-1)*height[n])
            # print i,ans,s
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.maximalRectangle(["01","10"]),1)


if __name__ == '__main__':
    unittest.main()
