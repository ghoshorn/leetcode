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