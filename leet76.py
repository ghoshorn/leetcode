# encoding: utf8
'''
Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

参考了https://leetcode.com/discuss/10337/accepted-o-n-solution
设置bool数组need，表示某字母是否出现在t里
数组require，表示某字母还需要出现多少次
count=len(t)，表示还有几个字母需要出现
滑动窗口[i,j]，
    如果count>0，则窗口扩大（右端向后滑）：
        新加入窗口的字母s[j],如果require[s[j]]>0，则count-=1; 如果s[j]在need数组中，则其需要的次数应该减少1，即require[s[j]]-=1；
    否则(count<=0)，说明窗口中的字母已经全部包含t，则win_min=min(j-i,win_min)，然后窗口缩小（左端后滑）：
        滑出窗口的字母s[i]，如果s[i]在need中，则需要增加其需要的次数，即require[s[j]]+=1；且如果此时即require[s[j]]>0，说明该字母还需要1次，令count+=1
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        require={}
        need={}
        for x in t:
            require[x]=require.get(x,0)+1
            need[x]=True
        count=len(t)
        l=len(s)
        i=0 #left
        j=0 #right
        win_min=l+1
        print l
        while j<=l and i<l:
            # print s[i:j+1],i,j,count,require
            if j==l and count>0:
                break
            if count>0:
                if require.get(s[j],0)>0:
                    count-=1
                if s[j] in need:
                    require[s[j]]-=1
                j+=1
            else:
                if win_min>j-i:
                    win_left=i
                    win_min=j-i
                if s[i] in need:
                    require[s[i]]+=1
                if require.get(s[i],0)>0:
                    count+=1
                i+=1
        if win_min==l+1:
            return ''
        else:
            return s[win_left:win_left+win_min]

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.minWindow('ADOBECODEBANC','ABC'),'BANC')


if __name__ == '__main__':
    unittest.main()
