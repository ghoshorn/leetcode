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
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        l=len(num)
        for i in range(l-1,0,-1):
            for j in range(i-1,-1,-1):
                # print j,i
                if num[j]<num[i]:
                    break
            if j==0 and i==1 and num[j]>=num[i]:
                num.reverse()
                return None
            if num[j]<num[i]:
                tmp=num[i:]
                # num=num[:i]
                print num
                for k in range(l-i):
                    num.pop()
                    print num
                tmp=tmp[::-1]
                print j,'---',tmp
                for x in tmp:
                    num.insert(j,x)
                    print num
                tmp=num[j+1:]
                tmp.sort()
                for k in range(j+1,l):
                    num[k]=tmp[k-j-1]
                    print num
                # print num
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
      

