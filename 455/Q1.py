import math
from typing import  List

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        d = dict()
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
        
        flag = False
        while not flag:
            for _, times in d.items():
                if times <= 1:
                    continue
                if times == 2:
                    flag = True
                    break
                for j in range(2, int(times ** 0.5) + 1):
                    print(j)
                    
                    if times % j == 0:
                        break
                else:
                    flag = True
            break
        return flag


nums = [3,3,0,3,3,6]

s = Solution()
r = s.checkPrimeFrequency(nums)
print(r)