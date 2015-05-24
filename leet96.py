# encoding: utf8
'''
Unique Binary Search Trees 
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

前几项为
n   ans
0   1
1   1
2   2
3   5
...
有点像catalan数。

利用Catalan的递推式h(n)=h(n-1)*(4*n-2)/(n+1)
'''

import unittest
from pprint import pprint
import pdb


class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n==0:
            return 1
        x=1
        for i in range(1,n+1):
            x=x*(4*i-2)/(i+1)
        return x

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.numTrees(1),1)
        self.assertEqual(self.a.numTrees(2),2)
        self.assertEqual(self.a.numTrees(3),5)


if __name__ == '__main__':
    unittest.main()