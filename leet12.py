# encoding: utf8
'''Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

记数方法
1、相同的数字连写，所表示的数等于这些数字相加得到的数，如：Ⅲ = 3；
基本字符 相应的阿拉伯数字表示
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

2、小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数， 如：Ⅷ = 8；Ⅻ = 12；
3、小的数字，（限于Ⅰ、X 和C）在大的数字的左边，所表示的数等于大数减小数得到的数，如：Ⅳ= 4；Ⅸ= 9；
4、正常使用时，连写的数字重复不得超过三次。（表盘上的四点钟“IIII”例外）
5、在一个数的上面画一条横线，表示这个数扩大1000倍。
对照举例
编辑

个位数举例
Ⅰ,1 】Ⅱ，2】 Ⅲ，3】 Ⅳ，4 】Ⅴ，5 】Ⅵ，6】Ⅶ，7】 Ⅷ，8 】Ⅸ，9 】
十位数举例
Ⅹ，10】 Ⅺ，11 】Ⅻ，12】 XIII,13】 XIV,14】 XV,15 】XVI,16 】XVII,17 】XVIII,18】 XIX,19】 XX,20】 XXI,21 】XXII,22 】XXIX,29】 XXX,30】 XXXIV,34】 XXXV,35 】XXXIX,39】 XL,40】 L,50 】LI,51】 LV,55】 LX,60】 LXV,65】 LXXX,80】 XC,90 】XCIII,93】 XCV,95 】XCVIII,98】 XCIX,99 】
百位数举例
C,100】 CC,200 】CCC,300 】CD,400】 D,500 】DC,600 】DCC,700】 DCCC,800 】CM,900】 CMXCIX,999】
千位数举例
M,1000】 MC,1100 】MCD,1400 】MD,1500 】MDC,1600 】MDCLXVI,1666】 MDCCCLXXXVIII,1888 】MDCCCXCIX,1899 】MCM,1900 】MCMLXXVI,1976】 MCMLXXXIV,1984】 MCMXC,1990 】MM,2000 】MMMCMXCIX,3999】

从千位开始向个位 依此处理。
千位直接加M，其他的分为x >9的，左边添数表示相减；5<x<9的，右边舔数表示相加；x=4的，左边添数表示相减；x<4的，重复x遍即可。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @return a string
    def intToRoman(self, num):
        dic={}
        dic[1]="I"
        dic[5]="V"
        dic[10]="X"
        dic[50]="L"
        dic[100]="C"
        dic[500]="D"
        dic[1000]="M"
        roman=""
        while num>=1000:
            roman+="M"
            num-=1000
        base=100
        while  num>0:
            if base==0:
                break
            if num<base:
                base=base/10
                continue
            if num>=5*base:
                if num>=9*base:
                    roman=roman+(num-8*base)/base*dic[base]+dic[base*10]
                else:
                    roman=roman+dic[base*5]+(num-5*base)/base*dic[base]
            else:
                if num>=4*base:
                    roman=roman+dic[base]+dic[base*5]
                else:
                    roman=roman+(num/base)*dic[base]
            num=num- num / base * base
            base=base / 10
        return roman


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.intToRoman(1),"I")
        self.assertEqual(self.a.intToRoman(5),"V")
        self.assertEqual(self.a.intToRoman(10),"X")
        self.assertEqual(self.a.intToRoman(39),"XXXIX")
        self.assertEqual(self.a.intToRoman(400),"CD")
        self.assertEqual(self.a.intToRoman(1900),"MCM")
        self.assertEqual(self.a.intToRoman(1666),"MDCLXVI")
        self.assertEqual(self.a.intToRoman(1888),"MDCCCLXXXVIII")
        self.assertEqual(self.a.intToRoman(1984),"MCMLXXXIV")


if __name__ == '__main__':
    unittest.main()