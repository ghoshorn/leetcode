# encoding: utf8
'''
Anagrams
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.

不是说，把这组里的回文词都挑出来，也不是说把这组里两个可以构成回文的挑出来。
而是说，组成两个单词的字母相同，顺序不同即可。。
Input:  ["ant","ant"]
Expected:   ["ant","ant"]

把每个单词的组成字母重新排序，作为新的单词加入字典。如果超过2次则说明存在anagrams。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        ans=[]
        dic={}
        for x in strs:
            xx=''.join(sorted(x))
            dic[xx]=dic.get(xx,0)+1
        # pprint(dic)
        for x in strs:
            xx=''.join(sorted(x))
            if dic[xx]>1:
                ans.append(x)
        # print(ans)
        return ans



class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.anagrams(['abc','aba','cba']),['abc','cba'])
        self.assertEqual(self.a.anagrams(['']),[])
        self.assertEqual(self.a.anagrams(["",""]),["",""])
        self.assertEqual(self.a.anagrams(['a']),[])
        self.assertEqual(self.a.anagrams(["c","c"]),["c","c"])


if __name__ == '__main__':
    unittest.main()


