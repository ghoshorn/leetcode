# encoding: utf8
'''
3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

复杂度O(n*n*log(n))，超时(⊙o⊙) 
这种题的复杂度不能比O(n*n)更小了吧？ 超时的话，感觉应该是加入列表并判重比较耗费时间。换一种判重思路可通过
需要注意，不能写为if j<l-1 and a[j]==a[j+1]，否则[0,0,0]这种情况将得不到解。
'''

import unittest
from pprint import pprint
import pdb

class Solution1:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        a=sorted(num)
        l=len(a)
        lst=[]
        for i in xrange(l-3):
            try:
                if a[i]==a[i-1]:
                    continue
            except Exception, e:
                pass
            for j in xrange(i+1,l-2):
                flag=False
                start=j+1
                end=l-1
                while start<=end:
                    mid=(start+end)/2
                    if a[mid]==-a[i]-a[j]:
                        flag=True
                        break
                    elif a[mid]>-a[i]-a[j]:
                        end=mid-1
                    else:
                        start=mid+1
                if flag:
                    lst.append( [a[i],a[j],-a[i]-a[j]] )
        return lst

class Solution2:
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
    def threeSum(self, num):
        a=sorted(num)
        l=len(a)
        lst=[]
        for i in range(l-2):
            for j in range(i+1,l-1):
                if self.find(a,j+1,l-1,-a[i]-a[j]):
                    if [a[i],a[j],-a[i]-a[j]] not in lst:
                        lst.append( [a[i],a[j],-a[i]-a[j]] )
        return lst

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
    def threeSum(self, num):
        a=sorted(num)
        l=len(a)
        lst=[]
        for i in range(l-2):
            if i>=1 and a[i-1]==a[i]:
                continue
            for j in range(i+1,l-1):
                if j!=i+1 and a[j]==a[j-1]:
                    continue
                if self.find(a,j+1,l-1,-a[i]-a[j]):
                    lst.append( [a[i],a[j],-a[i]-a[j]] )
                    # print i,j
        # print
        return lst

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.threeSum([-1,0,1,2,-1,-4]),[[-1,-1,2],[-1,0,1]] )
        self.assertEqual(self.a.threeSum([-1,0,1,2,-1,-4,-1]),[[-1,-1,2],[-1,0,1]] )
        self.assertEqual(self.a.threeSum([]),[] )
        self.assertEqual(self.a.threeSum([0,0,0]),[[0,0,0]] )
        self.assertEqual(self.a.threeSum([0,0,0,0]),[[0,0,0]] )
        # self.assertEqual(self.a.threeSum([7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]),[[-15, 1, 14],[-15, 2, 13],[-15, 3, 12]] )


if __name__ == '__main__':
    unittest.main()