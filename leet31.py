# encoding: utf8
'''
Next Permutation  
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

算法分三个步骤：

一般而言，设P是[1,n]的一个全排列。

1.  P=P1P2…Pn=P1P2…Pj-1PjPj+1…Pk-1PkPk+1…Pn

j=max{i|Pi<Pi+1},k=max{i|Pi>Pj}

2.  对换Pj，Pk，将Pj+1…Pk-1PjPk+1…Pn翻转，

3. P’= P1P2…Pj-1PkPn…Pk+1PjPk-1…Pj+1即P的下一个。

[注意]：在函数中，如果对传入的参数num适用操作 num=num[:i]，则num会变为新申请的内存，不会修改原num的值
    []运算开辟新空间进行操作!

'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        l=len(num)
        j=-1
        for i in range(0,l-1):
            if num[i]<num[i+1]:
                j=i
        if j==-1:
            num.reverse()
            return None
        for i in range(l-1,j,-1):
            if num[i]>num[j]:
                k=i
                break
        num[k],num[j]=num[j],num[k]
        self.reverse(num,j+1,l-1)
        return None

    def reverse(self,s,start,end):
        i=start
        j=end
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return None


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=Solution()

        x=[1,2,3]
        a.nextPermutation(x)
        self.assertEqual(x,[1,3,2])

        x=[1,1,5]
        a.nextPermutation(x)
        self.assertEqual(x,[1,5,1])

        x=[3,2,1]
        a.nextPermutation(x)
        self.assertEqual(x,[1,2,3])

        x=[1,3,2]
        a.nextPermutation(x)
        self.assertEqual(x,[2,1,3])

        x=[2,3,1]
        a.nextPermutation(x)
        self.assertEqual(x,[3,1,2])

        x=[5,4,7,5,3,2]
        a.nextPermutation(x)
        self.assertEqual(x,[5, 5, 2, 3, 4, 7])

        x=[2,2,7,5,4,3,2,2,1]
        a.nextPermutation(x)
        self.assertEqual(x,[2,3,1,2,2,2,4,5,7])

        x=[4,2,0,2,3,2,0]
        a.nextPermutation(x)
        self.assertEqual(x,[4,2,0,3,0,2,2])

if __name__ == '__main__':
    unittest.main()
      

