# encoding: utf8
'''
Permutation Sequence 
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

直接DFS超时。
先求n!，判断k离0和n!哪边近：如果离n!近，直接倒着数n!-k+1个。 时间减半，但还超时。（Solution1）

对于9位的排列来说，使用一点小trick吧，第一位就是1-9，dfs后八位。（Solution2）
对于8, 35784这种数据，耗时0.087s，居然还是超时。。

注定要用数学的方法了。。
由（Solution2）中的n9=[0,1,40321,80641,120961,161281,201601,241921,282241,322561]，
其中40321 =8!+1
    80641 =8!*2+1
    ...
对应第一位即为k/(n-1)!
第一位找到后，令k=k%(n-1)!，开始找第二位k/(n-2)!
'''

import unittest
from pprint import pprint
import pdb

class Solution1:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        self.n=n
        from math import factorial
        allcnt=factorial(n)
        if k<=allcnt/2:
            self.start    =1
            self.end      =n+1
            self.interval =1
            self.k        =k
        else:
            self.start    =n
            self.end      =0
            self.interval =-1
            self.k        =allcnt-k+1
        self.valid       =[True for i in range(n+1)]
        self.permutation =[0 for i in range(n)]
        self.ans=[]
        self.dfs(0)
        # print n,k,self.ans
        # print ''.join(map(lambda x:str(x),self.ans))
        return ''.join(map(lambda x:str(x),self.ans))

    def dfs(self, kth):
        if kth==self.n:
            # print self.permutation
            self.k-=1
            if self.k==0:
                self.ans=self.permutation
                return True
        for i in range(self.start,self.end,self.interval):
            if self.valid[i]:
                self.valid[i]=False
                self.permutation[kth]=i
                ret=self.dfs(kth+1)
                if ret:
                    return True
                self.valid[i]=True

class Solution2:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        self.n=n
        from math import factorial
        allcnt=factorial(n)
        self.k=k
        self.valid       =[True for i in range(n+1)]
        self.permutation =[0 for i in range(n)]
        self.ans=[]
        n9=[0,1,40321,80641,120961,161281,201601,241921,282241,322561]
        n9a=[
            [],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 1, 3, 4, 5, 6, 7, 8, 9],
            [3, 1, 2, 4, 5, 6, 7, 8, 9],
            [4, 1, 2, 3, 5, 6, 7, 8, 9],
            [5, 1, 2, 3, 4, 6, 7, 8, 9],
            [6, 1, 2, 3, 4, 5, 7, 8, 9],
            [7, 1, 2, 3, 4, 5, 6, 8, 9],
            [8, 1, 2, 3, 4, 5, 6, 7, 9],
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
        ]
        if n==9:
            for i in range(9,0,-1):
                if k>=n9[i]:
                    self.k=self.k-n9[i]+1
                    self.valid[i]=False
                    self.permutation[0]=i
                    # self.permutation=n9a[i]
                    self.dfs(1)
                    return ''.join(map(lambda x:str(x),self.ans))
        self.cnt=0
        self.dfs(0)
        # print n,k,self.ans
        # print ''.join(map(lambda x:str(x),self.ans))
        return ''.join(map(lambda x:str(x),self.ans))

    def dfs(self, kth):
        if kth==self.n:
            # print self.permutation
            # self.cnt+=1
            # if ''.join(map(lambda x:str(x),self.permutation))=='912345678':
            #     print self.cnt,self.permutation
            self.k-=1
            if self.k==0:
                self.ans=self.permutation
                return True
        for i in range(1,self.n+1):
            if self.valid[i]:
                self.valid[i]=False
                self.permutation[kth]=i
                ret=self.dfs(kth+1)
                if ret:
                    return True
                self.valid[i]=True

class Solution3:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        from math import factorial
        ans=[0 for i in range(n)]
        valid=[True for i in range(n+1)]
        k-=1 #why?
        for i in range(n):
            kth=k/factorial(n-i-1)+1
            cnt=0
            for j in range(1,n+1):
                if valid[j]:
                    cnt+=1
                    if cnt==kth:
                        ans[i]=j
                        valid[j]=False
            k=k%factorial(n-i-1)
        return ''.join(map(lambda x:str(x),ans))
        


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution3()

    def testLeet(self):
        self.assertEqual(self.a.getPermutation(3,1),'123')
        self.assertEqual(self.a.getPermutation(3,3),'213')
        self.assertEqual(self.a.getPermutation(3,6),'321')
        self.assertEqual(self.a.getPermutation(8, 15025),'38721456')
        self.assertEqual(self.a.getPermutation(9, 322561),'912345678')
        self.assertEqual(self.a.getPermutation(9, 362880),'987654321')
        

if __name__ == '__main__':
    unittest.main()
