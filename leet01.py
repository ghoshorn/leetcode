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
        nums=zip(num[:],range(len(num)))
	s=sorted(nums,key=lambda nums:nums[0])
	#print s
        i=0
        j=len(s)-1
        while i<j:
            tmp=s[i][0]+s[j][0]
            if tmp==target:
		i,j=s[i][1]+1,s[j][1]+1
                if i>j:
                    i,j=j,i
                return (i,j)
            elif tmp>target:
                j-=1
            else:
                i+=1

a=Solution()
print a.twoSum([2,7,11,15],9)
print a.twoSum([3,2,4],6)

