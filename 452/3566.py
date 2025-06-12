# https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/description/
# You are given an integer array nums containing distinct positive integers and an integer target.
#
# Determine if you can partition nums into two non-empty disjoint subsets,
# with each element belonging to exactly one subset,
# such that the product of the elements in each subset is equal to target.
#
# Return true if such a partition exists and false otherwise.
#
# A subset of an array is a selection of elements of the array.
# nums = [3,1,6,8,4], target = 24

from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        prod = 1
        squared = target * target
        for i in range(n):
            prod *= nums[i]
            if prod > squared:
                return False
        if prod != squared:
            return False
        maxi = 1 << n
        # for each value in range [0, maxi], means a subset of nums
        # 0 - means empty subset
        # maxi - means include all elem in nums
        # bitwise
        for i in range(1, maxi):
            prod = 1
            for j in range(n):
                if i & (1 << j):
                    prod *= nums[j]
                    if prod > target:
                        break
            if prod == target:
                return True
        return False

# recursive backtracking
# dynamic programming?
# subp:
class Solution2:
    def _solve(self, i: int, prod: int, target: int, nums: List[int]):
        if prod > target: return False
        if prod == target: return True
        if i >= len(nums): return False
        
        # include nums[i]
        self._solve(i+1, prod*nums[i], target, nums)
        # exclude nums[i]
        self._solve(i+1, prod, target, nums)
        return False
        
        
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        prod = 1
        squared = target * target
        for i in range(n):
            prod *= nums[i]
            if prod > squared:
                return False
        if prod != squared:
            return False
        
        return self._solve(0, 1, target, nums)
        
class Solution3:
    def checkEqualPartitons(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        d = [[1 for _ in range(n+1)] for _ in range(n+1)]
        for i in reversed(range(n)):
            subset = []
            for j in reversed(range(n)):
                # nums[i] is excluded?
                x = d[i][j+1] * nums[j]
                if j == i or x > target:
                    d[i][j] = d[i][j+1]
                else:
                    d[i][j] = x
                    subset.append(j)
            if d[i][0] == target:
                remained = 1
                for i in range(n):
                    if i in subset:
                        continue
                    remained *= nums[i]
                if remained == target:
                    return True
        return False

            
        

if __name__ == '__main__':
    nums = [3, 2, 7, 5]
    target =15
    sol3 = Solution3()
    r3 = sol3.checkEqualPartitons(nums, target)
    print(r3)
        
        
        

        