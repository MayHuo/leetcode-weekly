# Inverse Coin change

from typing import List

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        # i - total
        # nums[i] - ways to get total by using expected set of nums
        result = []
        for i in range(len(numWays)):
            # i+1
            if numWays[i] == 0:
                continue
            ways = numWays[i]
            while ways > 0:
                for j in result:
                    pass
                
            
            
            
                
            