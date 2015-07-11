# encoding: utf8
'''
Largest Number 
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

实质就是写一个比较函数。
例如
3 > 30
8308 > 830
83081 < 830
3 = 33
121 < 12

比较的时候，如果两个数一样长就好说了。
如果不一样长，是不是短的就是应该大呢？
（最开始这么认为的，例如3>30，但是显然不对！例如8308>830）
而是应该循环比较！

另一种比较方法（from剑指offer）
例如数字a,b
直接比较ab?ba的大小即可（转换为字符串比较即可）
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        all0=True
        for x in nums:
            if x!=0:
                all0=False
        if all0:
            return '0'
        nums_str=[str(x) for x in nums]
        nums_str.sort(reverse=True,cmp=self.compare)
        # print nums_str
        return ''.join(nums_str).replace(':','')
        
    def compare(self, a, b):
        la=len(a)
        lb=len(b)
        if a==b:
            return 0
        i=j=0
        while i<=la or j<=lb:
            if a[i%la]>b[j%lb]:
                return 1
            elif a[i%la]<b[j%lb]:
                return -1
            i+=1
            j+=1
        return 0 # in case of 3 vs 33

    def compare1(self, a, b): # wrong
        la=len(a)
        lb=len(b)
        i=j=0
        while i<la and j<lb:
            if a[i]>b[j]:
                return 1
            elif a[i]<b[j]:
                return -1
            i+=1
            j+=1
        if i<la:
            while i<la:
                if a[i]>b[0]:
                    return 1
                elif a[i]<b[0]:
                    return -1
                i+=1
            return -1
        if j<lb:
            while j<lb:
                if a[0]>b[j]:
                    return 1
                elif a[0]<b[j]:
                    return -1
                j+=1
            return 1
        return 0

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.largestNumber([3, 30, 34, 5, 9]), '9534330')
        self.assertEqual(self.a.largestNumber([9,98,97]), '99897')
        self.assertEqual(self.a.largestNumber([9,98,981]), '998981')
        self.assertEqual(self.a.largestNumber([121,12]), '12121')
        self.assertEqual(self.a.largestNumber([12,121]), '12121')
        self.assertEqual(self.a.largestNumber([1,1,1]), '111')
        self.assertEqual(self.a.largestNumber([0,0]), '0')
        self.assertEqual(self.a.largestNumber([4704,6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,5460,3399,9533,914,3932,192,3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,3636,6265,1518,8398]), "98909827968595339456944893859149094902689398937839883538183810810780707982784676057536747174237321720571007032685668066758674466986636554651163276306626562416221603859725909578457125682552954605422520849804812479847044453428339323905384638363699366436503636357535673516346233993298316330843021297028227452732697246523622362231322812216213206020001921763154815181495141713801147114310901048")
        self.assertEqual(self.a.largestNumber([9051,5526,2264,5041,1630,5906,6787,8382,4662,4532,6804,4710,4542,2116,7219,8701,8308,957,8775,4822,396,8995,8597,2304,8902,830,8591,5828,9642,7100,3976,5565,5490,1613,5731,8052,8985,2623,6325,3723,5224,8274,4787,6310,3393,78,3288,7584,7440,5752,351,4555,7265,9959,3866,9854,2709,5817,7272,43,1014,7527,3946,4289,1272,5213,710,1603,2436,8823,5228,2581,771,3700,2109,5638,3402,3910,871,5441,6861,9556,1089,4088,2788,9632,6822,6145,5137,236,683,2869,9525,8161,8374,2439,6028,7813,6406,7519]), "995998549642963295795569525905189958985890288238775871870185978591838283748308830827481618052787813771758475277519744072727265721971071006861683682268046787640663256310614560285906582858175752573156385565552654905441522852245213513750414822478747104662455545424532434289408839763963946391038663723370035134023393328828692788270926232581243924362362304226421162109163016131603127210891014")
        self.assertEqual(self.a.largestNumber([3,43,48,94,85,33,64,32,63,66]), '9485666463484333332')

if __name__ == '__main__':
    unittest.main()