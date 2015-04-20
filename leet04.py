'''
Median of Two Sorted Arrays

There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
最初想法是，设置ia,ja,ib,jb四个指针分别指向A和B的头和尾，首先检查 是否某个数组全部大于另一个数组，可直接计算返回；否则，每次比较头部两个数字并将小的后移，比较尾部两个并将大的前移，指导头尾相遇。不过发现其中需要太多的判断，代码超过70行还是不能把所有情况都考虑到。。。



然后换做，找到第k和k+1大的数（如果一共2n+1个数，找到第k个就可以；如果一共2n个，则需要找到k和k+1求平均），其中k就是中位数。

考虑到len(A)+len(B)可能奇数或偶数，并且有时候需要同时找到第k+1个，因此取

k=(len(A)+len(B)+1)/2+1。 比如如果一共5个数，k=(5+1)/2+1=4，即找到第3,4大的数；一共6个数，k=(6+1)/2+1=4，即找到第3,4大的数。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @return a float
    def findMedianSortedArrays0(self, A, B):
        la=len(A)
        lb=len(B)
        if la==lb==1:
            return (A[0]+B[0])/2.0
        if A==[]:
            if lb%2==1:
                return B[(lb+1)/2-1]
            else:
                return (B[lb/2]+B[lb/2-1])/2.0
        if B==[]:
            if la%2==1:
                return A[(la+1)/2-1]
            else:
                return (A[la/2]+A[la/2-1])/2.0

        if B[lb-1]<A[0]:
            A,B=B,A
            la,lb=lb,la
        if A[la-1]<B[0]:
            l=la+lb
            if l%2==1:
                pos=(l+1)/2
                if pos<=la:
                    return A[pos-1]
                else:
                    return B[pos-la-1]
            else:
                pos=l/2
                if pos<=la:
                    tmp1= A[pos-1]
                else:
                    tmp1= B[pos-la-1]
                pos=l/2+1
                if pos<=la:
                    tmp2= A[pos-1]
                else:
                    tmp2= B[pos-la-1]
                return (tmp1+tmp2)/2.0
        ia=ib=0
        ja=la-1
        jb=lb-1
        # pdb.set_trace()
        while ia<ja and ib<jb:
            if A[ia]<B[ib]:
                ia+=1
            else:
                ib+=1
            if ia<=ja and ib<=jb:
                if A[ja]>B[jb]:
                    ja-=1
                else:
                    jb-=1
            elif ia<ja:
                ja-=1
            elif ib<jb:
                jb-=1
        while ia<ja-1:
            ia+=1
            ja-=1
        while ib<jb-1:
            ib+=1
            jb-=1
        if ia==ja and ib==jb:
            return (A[ia]+B[ib])/2.0
        if ia==ja:
            return A[ia]
        elif ia==ja-1:
            return (A[ia]+A[ja])/2.0
        elif ib==jb:
            return B[ib]
        else:
            return (B[ib]+B[jb])/2.0

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        la=len(A)
        lb=len(B)
        if A==[]:
            if lb%2==1:
                return B[(lb+1)/2-1]
            else:
                return (B[lb/2]+B[lb/2-1])/2.0
        if B==[]:
            if la%2==1:
                return A[(la+1)/2-1]
            else:
                return (A[la/2]+A[la/2-1])/2.0
        l=la+lb
        n=(l+1)/2+1
        ia=ib=cnt=k=k2=0
        while cnt<n:
            if ib>=lb or ia<la and A[ia]<B[ib]:
                k=k2
                k2=A[ia]
                ia+=1
            else:
                k=k2
                k2=B[ib]
                ib+=1
            cnt+=1
        if l%2==1:
            return k
        else:
            return (k+k2)/2.0

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.findMedianSortedArrays([4,5,6,7],[1,2,3]),4)
        self.assertEqual(self.a.findMedianSortedArrays([1,3,5],[2,4,6,7]),4)
        self.assertEqual(self.a.findMedianSortedArrays([],[1]),1)
        self.assertEqual(self.a.findMedianSortedArrays([1,3,4],[2]),2.5)
        self.assertEqual(self.a.findMedianSortedArrays([1,3,4,5],[2]),3)
        self.assertEqual(self.a.findMedianSortedArrays([1,3,4,5,6],[2]),3.5)
        self.assertEqual(self.a.findMedianSortedArrays([], [2,3]),2.5)
        self.assertEqual(self.a.findMedianSortedArrays([], [2,3,4]),3)
        self.assertEqual(self.a.findMedianSortedArrays([1], [2]),1.5)
        self.assertEqual(self.a.findMedianSortedArrays([3], [1,2]),2)
        self.assertEqual(self.a.findMedianSortedArrays([1], [2,3,4]),2.5)
        self.assertEqual(self.a.findMedianSortedArrays([2], [1,3,4]),2.5)
        

if __name__ == '__main__':
    unittest.main()