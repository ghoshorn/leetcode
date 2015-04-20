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

