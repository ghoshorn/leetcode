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

