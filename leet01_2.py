# encoding: utf8
'''
Two Sum

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

思路：先排序；再从两头向中间找 O(nlogn)
'''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d={}
        for i in xrange(len(num)):
            if target-num[i] in d:
                return(d[target-num[i]]+1,i+1)
            d[num[i]]=i
        # d={}
        # d2={}
        # for i in xrange(len(num)):
        #     if num[i] not in d:
        #         d[num[i]]=i
        #     else:
        #         d2[num[i]]=i
        # print d,d2
        # for x in num:
        #     if target-x in d:
        #         if target-x in d2:
        #             return(d[x]+1,d2[target-x]+1)
        #         elif x!=target-x:
        #             return(d[x]+1,d[target-x]+1)

a=Solution()
print a.twoSum([2,7,11,15],9)
print a.twoSum([3,2,4],6)
print a.twoSum([0,4,3,0],0)
print a.twoSum([3,2,4], 6)

