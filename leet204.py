# encoding: utf8
'''
Count Primes 
Description:

Count the number of prime numbers less than a non-negative number, n.

Hint:

Let's start with a isPrime function. To determine if a number is prime, we need to 
check if it is not divisible by any number less than n. The runtime complexity of 
isPrime function would be O(n) and hence counting the total prime numbers up to n 
would be O(n2). Could we do better?
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n<=2:
            return 0
        f=[True for i in range(n+1)]
        f[0]=False
        f[1]=False
        f[n]=False
        for i in xrange(2,n):
            if f[i]:
                for j in xrange(2,n/i+1):
                    f[i*j]=False
        # print f
        return f.count(True)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.countPrimes(3), 1)
        self.assertEqual(self.a.countPrimes(4), 2)
        self.assertEqual(self.a.countPrimes(5), 2)
        self.assertEqual(self.a.countPrimes(999983), 78497)


if __name__ == '__main__':
    unittest.main()