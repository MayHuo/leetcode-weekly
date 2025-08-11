# Given a string s of length n
# An integer array order is a permutation of the numbers in the range [0, n-1]
# Starting from time t = 0, replace s[order[t]] = "*" at each time step
# A substring is valid if it contains at least one "*"
# String s is active if the total number of valid substring  >= k
# Return the minimum time t at which the string s becomes active, return -1 if it is impossible

from typing import List

# total number of valid substring -- dynamic programming, SRTBOT
# SubPro: dp[i] is the number of invalid substring starting at s[i]
# Relation:
## If s[i] == "*": dp[i] = 0
## Else dp[i] = dp[i+1] + 1; For single substring of s[i]
# Topo: decreasing i
# Base: dp[n] = 0
# Original: dp[0]
# Total Invalid = sum(dp)

# total number of valid substring = total number - invalid number = n * (n+1) // 2 - dp[0]
# For a string of length n, the number of substrings can be derived like this:
# From position 0: n substrings, s[0:i] for i = 1 to i = n -- n
# From position 1: n-1 substring, s[1:i] for i = 2 to n -- n - 1
# ...
# From position n-1: 1 substring, s[n-1: i] for i = n to n -- 1


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        # valid substring -- dynamic programming
        n = len(s)
        slist = [c for c in s]
        dp = [0] * (n+1)
        def invalid_substring(l: List[str]):
            nonlocal dp
            for i in reversed(range(len(l))):
                if l[i] == "*":
                    dp[i] = 0
                else:
                    dp[i] = dp[i+1] + 1
            return sum(dp)

        total_substr = n * (n+1) // 2
        if total_substr < k:
            return -1
        # dynamic_invalid[i] is the number of invalid substrings ending at i
        dynamic_invalid = [0] * n
        invalid = 0
        count = 0
        for i in range(n):
            if s[i] == "*":
                count = 0
            else:
                count += 1
                invalid += count
            dynamic_invalid[i] = invalid
        print(dynamic_invalid, invalid)
        t = 0
        valid = total_substr - invalid
        # Don't recalculate invalid for each replacement
        # invalid -= valids by s[i] = "*"
        while valid < k:
            idx = order[t]
            slist[idx] = "*"
            offset = dynamic_invalid[idx]
            dynamic_invalid[idx] = 0
            right = idx + 1
            while s[right] != "*":
                dynamic_invalid[right] -= offset
        
        return t
        
            
        
        
solution = Solution()
s = "abc"
order = [1, 2, 0]
k = 4
result = solution.minTime(s, order, k)
print(result)

