from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        p = 0
        q = n-1
        
        while p < q:
            if nums[p] >= nums[p+1]:
                break
            p += 1
        if not (0 < p < q):
            return False
        q = p
        while q < n-1:
            if nums[q] <= nums[q+1]:
                break
            q += 1
        if not q < n-1:
            return False
        for i in range(q+1, n):
            if nums[i-1] >= nums[i]:
                return False
        return True
        
            
        
            
            
        for i in range(q+1, n):
            if nums[i] <= nums[i-1]:
                return False
        return (0 < p < q) and (q < n-1)
        
                
    
nums = [1,3,5,4,2,6]
# nums = [2, 1, 3]
s = Solution()
result = s.isTrionic(nums)
print(result)