# encoding: utf8
'''
Edit Distance
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

DP.
需要注意初始化条件。Line 38,43.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        l1=len(word1)
        l2=len(word2)
        if l1==0:
            return l2
        elif l2==0:
            return l1
        distance=[[0 for i in range(l1)] for j in range(l2)]
        if word1[0]!=word2[0]:
            distance[0][0]=1
        for i in range(1,l1):
            if word1[i]!=word2[0]:
                distance[0][i]=distance[0][i-1]+1
            else:
                distance[0][i]=i #distance[0][i-1]
        for j in range(1,l2):
            if word2[j]!=word1[0]:
                distance[j][0]=distance[j-1][0]+1
            else:
                distance[j][0]=j #distance[j-1][0]
        for i in range(1,l2):
            for j in range(1,l1):
                if word1[j]==word2[i]:
                    distance[i][j]=distance[i-1][j-1]
                else:
                    distance[i][j]=min(distance[i-1][j],distance[i][j-1],distance[i-1][j-1])+1
        # for line in distance:
        #     print line
        # print 
        return distance[l2-1][l1-1]


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.minDistance("abc","abc"),0)
        self.assertEqual(self.a.minDistance("abc","adc"),1)
        self.assertEqual(self.a.minDistance("a","ad"),1)
        self.assertEqual(self.a.minDistance("mart", "karma"),3)
        self.assertEqual(self.a.minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"),27)


if __name__ == '__main__':
    unittest.main()
