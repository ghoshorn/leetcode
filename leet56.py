# encoding: utf8
'''
Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

思路：
首先按照intervals.start排序。然后从头开始比较intervals[i].end和intervals[i+1].start的大小，
发现重叠情况，则把intervals[i].end=max(intervals[i].end,intervals[i+1].end)，然后删除i+1。

由于区间采用的是class，assertEqual会判断是否为同一个对象。只能打印出来看结果了，AC。
'''

import unittest
from pprint import pprint
import pdb

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        intervals=sorted(intervals,lambda x,y:cmp(x.start,y.start))
        i=0
        while i<len(intervals)-1:
            if intervals[i].end>=intervals[i+1].start:
                intervals[i].end=max(intervals[i].end,intervals[i+1].end)
                del(intervals[i+1])
            else:
                i+=1
        for x in intervals:
            print x.start,x.end
        return intervals

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]),\
                                [Interval(1,6),Interval(8,10),Interval(15,18)])

if __name__ == '__main__':
    unittest.main()
