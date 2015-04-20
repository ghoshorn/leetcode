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