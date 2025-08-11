# Dynamic Programming approach
# Equal length of word1, word2
# Divide word1 into substrs, then do operations below
# operations: Replace one character, Swap two characters, Reverse
## SRTBOT
# How to divide?
# x(i) - minimum operation to transform word1[i:] to word2[i:]
# i != j math.inf
# if word1[i] == word2[j]: x(i+1, j+1)
# elif (is Swap works? is Reverse works?) word1[i] = word2[i+1] and word1[i+1] = word2[i] swap works : 1 + x(i+2)
# reverse? how to check reverse?
# do reverse for word1[i:] then compare to word2[i:]
# fedc, dabc; fedcb, edabc; fedcba, fedabc
# Difficult

def without_reverse(str1, str2):
    if len(str1) != len(str2):
        return float('inf')
    n = len(str1)
    dp = [0] * (n+2)
    
    # str1[i:] str2[i:]
    for i in reversed(range(n)):
        if str1[i] == str2[i]:
            dp[i] = dp[i+1]
        else:
            if i+1 < n and str1[i] == str2[i+1] and str1[i+1] == str2[i]:
                dp[i] = min(1+dp[i+2], 1+dp[i+1])
            else:
                dp[i] = 1 + dp[i+1]
    print(dp)
    return dp[0]
        
    
if __name__ == '__main__':
    str1 = 'fedcb'
    str2 = 'edabc'
    r = without_reverse(str1, str2)
    print(r)
