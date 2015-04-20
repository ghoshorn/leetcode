'''
ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
比如nRows=4

0        6            12
1    5   7       11   13
2 4      8   10       14
3        9            15

第一行间隔是 (nRows-1)*2=(4-1)*2=6

之后的间隔是 
4,2
2,4
6,0
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @return a string
    def convert(self, s, nRows):
        l=len(s)
        if l==0 or l==1 or nRows==1 or l<=nRows:
            return s
        n=(nRows-1)*2
        ss=''
        interval1=n
        interval2=0
        for i in range(nRows):
            j=i
            ss=ss+s[j]
            while j<l:
                if interval1!=0:
                    j+=interval1
                    if j<l:
                        ss=ss+s[j]
                if interval2!=0:
                    j+=interval2
                    if j<l:
                        ss=ss+s[j]
            interval1-=2
            interval2+=2
        return ss

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.convert("PAYPALISHIRING", 3),'PAHNAPLSIIGYIR')
        self.assertEqual(self.a.convert("A", 1),'A')
        self.assertEqual(self.a.convert("AB", 1),'AB')
        self.assertEqual(self.a.convert("AB", 3),'AB')

if __name__ == '__main__':
    unittest.main()