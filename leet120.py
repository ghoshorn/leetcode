# encoding: utf8
'''
Triangle
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        l=len(triangle)
        ans=triangle[l-1]
        for i in range(l-2,-1,-1):
            for j in range(len(triangle[i])):
                ans[j]=triangle[i][j]+min(ans[j],ans[j+1])
            print(ans)
        return ans[0]

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        x=[[2],[3,4],[6,5,7],[4,1,8,3]]
        self.assertEqual(self.a.minimumTotal(x),11)

if __name__ == '__main__':
    unittest.main()