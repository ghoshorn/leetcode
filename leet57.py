# encoding: utf8
'''
Insert Interval 
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
注意intervals为空的情况，以及newInterval本身以及被包含的情况。
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
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        # intervals=sorted(intervals,lambda x,y:cmp(x.start,y.start))
        # if len(intervals)==0:
        #     return [newInterval]
        i=0
        while i<len(intervals):
            if intervals[i].start<=newInterval.start and newInterval.end<=intervals[i].end:
                return intervals
            elif intervals[i].start<=newInterval.start<=intervals[i].end:
                newInterval.start=min(intervals[i].start,newInterval.start)
                del(intervals[i])
            elif intervals[i].start<=newInterval.end<=intervals[i].end:
                newInterval.end=max(newInterval.end,intervals[i].end)
                del(intervals[i])
            elif intervals[i].start>=newInterval.start and intervals[i].end<=newInterval.end:
                del(intervals[i])
            else:
                i+=1
        if len(intervals)==0:
            return [newInterval]
        for i in range(len(intervals)):
            if intervals[i].start>newInterval.start:
                intervals.insert(i,newInterval)
                break
        else:
            intervals.insert(len(intervals),newInterval)
        # for x in intervals:
        #     print x.start,x.end
        # print '---'
        return intervals

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.a.insert([Interval(1,3),Interval(6,9)],Interval(2,5))
        # self.assertEqual()
        self.a.insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)],Interval(4,9))
        xx=self.a.insert([],Interval(2,5))
        for x in xx:
            print x.start,x.end
        print '---'
        xx=self.a.insert([Interval(1,5)],Interval(2,3))
        for x in xx:
            print x.start,x.end
        print '---'
        xx=self.a.insert([Interval(1,5)],Interval(2,7))
        for x in xx:
            print x.start,x.end
        print '---'
        xx=self.a.insert([Interval(1,5)],Interval(6,8))
        for x in xx:
            print x.start,x.end
        print '---'


if __name__ == '__main__':
    unittest.main()
