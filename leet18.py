'''
4Sum
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

类似于leetcode 15 3sum。采用类似的思路，O(n^3)，超时。。

在此基础上优化：
增加一个字典缓存exist={}，把每两个数的和都加入字典；如果target-a[i]-a[j]不在字典中，则不必继续查找。时间复杂度平均降到O(n^2)
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    def find(self,s,start,end,num):
        while start<=end:
            mid=(start+end)/2
            if s[mid]==num:
                return True
            elif s[mid]>num:
                end=mid-1
            else:
                start=mid+1
        return False

    # @return a list of lists of length 3, [[val1,val2,val3]]
    def fourSum(self, num, target):
        a=sorted(num)
        l=len(a)
        lst=[]
        exist={}
        for i in range(l-1):
            for j in range(l):
                exist[a[i]+a[j]]=True
        for i in range(l-3):
            if i>=1 and a[i-1]==a[i]:
                continue
            for j in range(i+1,l-2):
                if j!=i+1 and a[j]==a[j-1]:
                    continue
                if exist.get(target-a[i]-a[j],False):
                    for k in range(j+1,l-1):
                        if k!=j+1 and a[k]==a[k-1]:
                            continue
                        if self.find(a,k+1,l-1,target-a[i]-a[j]-a[k]):
                            lst.append( [a[i],a[j],a[k],target-a[i]-a[j]-a[k]] )
        return lst

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.fourSum([1,0,-1,0,-2,2],0),[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] )
        self.assertEqual(self.a.fourSum([-489,-475,-469,-468,-467,-462,-456,-443,-439,-425,-425,-410,-401,-342,-341,-331,-323,-307,-299,-262,-254,-245,-244,-238,-229,-227,-225,-224,-221,-197,-173,-171,-160,-142,-142,-136,-134,-125,-114,-100,-86,-81,-66,-47,-37,-34,4,7,11,34,60,76,99,104,113,117,124,139,141,143,144,146,157,157,178,183,185,189,192,194,221,223,226,232,247,249,274,281,284,293,298,319,327,338,340,368,375,377,379,388,390,392,446,469,480,490], 2738),[] )
        self.assertEqual(self.a.fourSum([-458,-442,-428,-421,-408,-402,-385,-377,-377,-318,-318,-298,-230,-225,-203,-150,-130,-125,-124,-106,-86,-71,-59,-11,-3,37,59,92,94,97,108,145,188,189,190,239,257,270,281,296,308,309,355,405,412,416,429,434,438,455,460,462,466,469], -6120),[] )


if __name__ == '__main__':
    unittest.main()