from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        mapping: dict[int, List] = dict()
        for i in range(n):
            if not mapping.get(nums[i]):
                mapping[nums[i]] = [i]
            else:
                mapping[nums[i]].append(i)
        
        for k, idx_of_k in mapping.items():
            t = k * 2
            if t not in mapping:
                continue
            
            if len(mapping[t]) < 2:
                continue
            idx_of_t = mapping[t]
            f = False
            for idx_k in idx_of_k:
                pass
                
                
                
        