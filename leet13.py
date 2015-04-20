import unittest
from pprint import pprint
import pdb

class Solution:
    # @return an integer
    def romanToInt(self, s):
        dic={}
        dic["I"]=1
        dic["V"]=5
        dic["X"]=10
        dic["L"]=50
        dic["C"]=100
        dic["D"]=500
        dic["M"]=1000
        lst=("I","V","X","L","C","D","M")
        num=0
        for i in range(len(s)):
            for j in lst:
                if j in s[i:]:
                    pivot=dic[j] #determin add or sub
            if dic[s[i]]>=pivot:
                num+=dic[s[i]]
            else:
                num-=dic[s[i]]
        return num

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.romanToInt("I"),1)
        self.assertEqual(self.a.romanToInt("V"),5)
        self.assertEqual(self.a.romanToInt("X"),10)
        self.assertEqual(self.a.romanToInt("XXXIX"),39)
        self.assertEqual(self.a.romanToInt("CD"),400)
        self.assertEqual(self.a.romanToInt("MCM"),1900)
        self.assertEqual(self.a.romanToInt("MDCLXVI"),1666)
        self.assertEqual(self.a.romanToInt("MDCCCLXXXVIII"),1888)
        self.assertEqual(self.a.romanToInt("MCMLXXXIV"),1984)


if __name__ == '__main__':
    unittest.main()