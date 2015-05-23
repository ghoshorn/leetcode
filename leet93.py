# encoding: utf8
'''
Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''

import unittest
from pprint import pprint
import pdb



class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        self.ans=[]
        self.s=s
        self.l=len(s)
        self.dfs([],1,0) # the 1st, from pos 0
        print self.ans
        return self.ans

    def dfs(self,now,k,pos):
        if k==5:
            if pos>=self.l:
                self.ans.append('.'.join(now))
            return
        for i in range(1,min(4,self.l-pos+1)):
            tmp=self.s[pos:pos+i]
            if 0<=int(tmp)<=255:
                if str(int(tmp))==tmp: # avoid sth like 0.1.001.0
                    self.dfs(now+[tmp],k+1,pos+i)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.restoreIpAddresses("25525511135"),["255.255.11.135", "255.255.111.35"])
        self.assertEqual(self.a.restoreIpAddresses("010010"),["0.10.0.10","0.100.1.0"])


if __name__ == '__main__':
    unittest.main()