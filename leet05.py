'''
Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
蛮力肯定超时，直接想DP吧。

【错】使用一个数组l, l[i]记录以s[i]结尾的字符串的最大回文长度。l[i]=i-j+1, if s[i]==s[j], i-l[i-1]-1<=j<i。 对于一部分数据比如bananas，abababa来说是对的，但是还有问题，比如aaabaaaa：当aaabaaa已经是回文的时候，最后一个a==第一个a，回文长度又会+1，但是显然是错误的。。

还是需要用二维数组记录回文的区间。

f[i,j]=true表示i-j是回文。则 f[i,j]=true if (i+1==j and s[i]==s[j]) or (f[i+1][j-1] and s[i]==s[j]). 时间复杂度O(n^2)。

[注]：第35行，如果写f=[[False]*l]*l，然后for i in range(l): f[i][i]=True，则会全部变成True！
算法对了，但是当len(s)=1000的时候还是超时。。

看了一些其他解答方法====

* 枚举对称轴，分别向两边检验。O(n^2)。

* s的逆序s'，转换为求s和s'的最长公共子串，且子串位置需保持一致。
'''

import unittest
from pprint import pprint
import pdb

class Solution1: #DP O(n*n)
    # @return a string
    def longestPalindrome(self, s):
        if s=='':
            return ''
        maxlen=1
        end=0
        l=len(s)
        f=[[False]*l for i in xrange(l)]
        for i in xrange(l):
            f[i][i]=True
        # pdb.set_trace()
        for i in xrange(l-1,-1,-1):
            for j in xrange(i+1,l):
                if (i+1==j and s[i]==s[j]) or (f[i+1][j-1] and s[i]==s[j]):
                    f[i][j]=True
                    if j-i+1>maxlen:
                        maxlen=j-i+1
                        end=j
        ss=s[end-maxlen+1:end+1]
        # pprint(f)
        # print end-maxlen+1,end,s,ss
        return ss

class Solution: #use LCS
    # @return a string
    def longestPalindrome(self, s):
        s1=s
        s2=s[::-1]
        l=len(s)
        f=[[0]*l for i in xrange(l)]
        for i in xrange(l):
            for j in xrange(l):
                if 

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.longestPalindrome('abcbde'),'bcb')
        self.assertEqual(self.a.longestPalindrome('a'),'a')
        self.assertEqual(self.a.longestPalindrome(''),'')
        self.assertEqual(self.a.longestPalindrome('aaaaa'),'aaaaa')
        self.assertEqual(self.a.longestPalindrome('bananas'),'anana')
        self.assertEqual(self.a.longestPalindrome('abababa'),'abababa')
        self.assertEqual(self.a.longestPalindrome('ababababababa'),'ababababababa')
        self.assertEqual(self.a.longestPalindrome('abababaabababa'),'abababaabababa')
        self.assertEqual(self.a.longestPalindrome('aabbaabbaa'),'aabbaabbaa')
        self.assertEqual(self.a.longestPalindrome('aaabaaaa'),'aaabaaa')
        self.assertEqual(self.a.longestPalindrome('zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez'),'zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez')
        self.assertEqual(self.a.longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'),'ranynar')
        self.assertEqual(self.a.longestPalindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'),'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        

if __name__ == '__main__':
    unittest.main()