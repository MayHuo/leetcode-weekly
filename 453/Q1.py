from typing import List

class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def count_flips(target: int) -> int:
            arr = nums[:]
            flips = 0
            for i in range(len(arr) - 1):
                if arr[i] != target:
                    arr[i] *= -1
                    arr[i+1] *= -1
                    flips += 1
            if all(x==target for x in arr):
                return flips
            return float('inf')
        return min(count_flips(1), count_flips(-1)) <= k
        
        

sol = Solution()
nums = [1,-1,1]
k = 2
r = sol.canMakeEqual(nums, k)
print(nums)
print(r)