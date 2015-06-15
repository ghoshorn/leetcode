# encoding: utf8
'''
Pascal's Triangle
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows==0:
            return []
        ans=[[1]]
        for i in range(2,numRows+1):
            tmp=[1]
            for j in range(2,i):
                tmp.append(ans[-1][j-2]+ans[-1][j-1])
            tmp.append(1)
            ans.append(tmp)
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        x=self.a.generate(8)
        pprint(x)

if __name__ == '__main__':
    unittest.main()