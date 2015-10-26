# encoding: utf8
'''
H-Index
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.

升序排序后，如果某个值大于等于他（包含）之后的元素个数，则这个元素个数肯定是一个hindex。
从前向后找到最大的一个即可。
时间复杂度为O(nlogn)

一种使用辅助空间O(n),时间O(n)的算法
https://leetcode.com/discuss/55952/my-o-n-time-solution-use-java
public int hIndex(int[] citations) {
        int length = citations.length;
        if (length == 0) {
            return 0;
        }

        int[] array2 = new int[length + 1];
        for (int i = 0; i < length; i++) {
            if (citations[i] > length) {
                array2[length] += 1;
            } else {
                array2[citations[i]] += 1;
            }
        }
        int t = 0;
        int result = 0;

        for (int i = length; i >= 0; i--) {
            t = t + array2[i];
            if (t >= i) {
                return i;
            }
        }
        return 0;
    }
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l=len(citations)
        if l==0:
            return 0
        citations.sort()
        for i in xrange(l):
            if l-i<=citations[i]:
                return l-i
        return 0

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.hIndex([3, 0, 6, 1, 5]),3)
        self.assertEqual(self.a.hIndex([0, 0]),0)
        self.assertEqual(self.a.hIndex([0]),0)
        self.assertEqual(self.a.hIndex([0,1]),1)

if __name__ == '__main__':
    unittest.main()