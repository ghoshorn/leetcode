# encoding: utf8
'''
Repeated DNA Sequences 
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

又是位运算了。
参考https://leetcode.com/discuss/24478/i-did-it-in-10-lines-of-c
The main idea is to store the substring as int in map to bypass the memory limits.

There are only four possible character A, C, G, and T, but I want to use 3 bits per letter instead of 2.

Why? It's easier to code.

A is 0x41, C is 0x43, G is 0x47, T is 0x54. Still don't see it? Let me write it in octal.

A is 0101, C is 0103, G is 0107, T is 0124. The last digit in octal are different for all four letters. That's all we need!

We can simply use s[i] & 7 to get the last digit which are just the last 3 bits, it's much easier than lookup table or switch or a bunch of if and else, right?

We don't really need to generate the substring from the int. While counting the number of occurrences, we can push the substring into result as soon as the count becomes 2, so there won't be any duplicates in the result.

vector<string> findRepeatedDnaSequences(string s) {
    unordered_map<int, int> m;
    vector<string> r;
    int t = 0, i = 0, ss = s.size();
    while (i < 9)
        t = t << 3 | s[i++] & 7;
    while (i < ss)
        if (m[t = t << 3 & 0x3FFFFFFF | s[i++] & 7]++ == 1)
            r.push_back(s.substr(i - 10, 10));
    return r;
}
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        l=len(s)
        ht={}
        ret=[]
        for i in range(l-10+1):
            tmp=s[i:i+10]
            x=self.toint(tmp)
            if ht.get(x,0)==1:
                ret.append(tmp)
            ht[x]=ht.get(x,0)+1
        return ret

    def toint(self, s):
        ret=0
        for x in s:
            ret=ret<<3 | ord(x) & 7
            # ret=(ret<<3) + (ord(x) & 7)
        return ret

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC", "CCCCCAAAAA"])
        self.assertEqual(self.a.findRepeatedDnaSequences("AAAAAAAAAAA"), ["AAAAAAAAAA"])

if __name__ == '__main__':
    unittest.main()