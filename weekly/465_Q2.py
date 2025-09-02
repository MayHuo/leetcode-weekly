# Given two integers n and k, split the number n into exactly k positive
# integers such that the product of these integers is equal to n.
#
# Return any one split in which the maximum difference between
# any two numbers is minimized. You may return the result in any order.©leetcode

from typing import List
import math


class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        def is_prime(x):
            if x == 2:
                return True
            for i in range(2, math.ceil(math.sqrt(x))+1):
                if x % i == 0:
                    return False
            return True
        factors = []
        primes = []
        def recurse(x, k):
            nonlocal factors
            print(x, k, factors)
            if k == 1:
                factors.append(x)
                return x
            
            if is_prime(x):
                # means x can only be divided by 1
                primes.append(x)
                if factors:
                   return recurse(factors.pop(0), k)
                return
            
            kr = math.floor(x ** (1/k))
            while x % kr != 0:
                kr -= 1
            if kr == 1:
                return recurse(x, k-1)
            else:
                factors.append(kr)
                return recurse(x // kr, k-1)
        
        recurse(n, k)
        results = factors + primes
        while len(results) < k:
            results.append(1)
        return results
        
s = Solution()
n = 20
k = 4
# For this test case, the leetcode answer is [1, 1, 4, 5],
# but I got a better answer as [5, 2, 2, 1]
# Both the maximum difference of any two elements is 4
r = s.minDifference(n, k)
print(r)



            
            
            