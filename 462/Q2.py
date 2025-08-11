# nums is a permutation of numbers in the range [0,n-1], n is the length of nums
# You may swap elements at indices i and j only if nums[i] & nums[j] == K
# & denotes the bitwise AND operation and k is a non-negative integer,
# Return the maximum value of k such that the array can be sorted
# in non-decreasing order using any number of such swaps.
# If nums is already sorted, return 0

# Break steps
# 1. Understanding the swap condition nums[i] & nums[j] == k
## For a given k, we can think of this as:
## We can connect two numbers if a & b == k
# 2. Graph interpretation
## If we treat each index as a node, and we draw an edge between two node if their value's AND equals k
## then the allowed swaps correspond to moving elements along edges in this graph.
## If the graph for k connects exactly the elements that need to be swapped to their target places, then we can sort.
# 3. For the maximum value of k
## The possible values of k are in 0 ... n-2
## 1). We can check from the largest possible k down to 0
## 2). For each k, build connectivity graph based on condition (a & b) == k
## 3). Check if the permutation can be sorted using only those edges

# Implementation
# 1. Build connectivity nodes of indices for each k from n-2 to 0
## If the connected nodes exactly the same elements that not in their target positions, then we can sort
## Complexity: Best Case: O(n^3)

# 2. Precompute positions of each value
## Then group values with (x & y) == k using Union-Find
## Then check if every element's value can be moved to its correct position ?? How

### Connected Component

from typing import List
import math

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        # Build connectivity graph
        n = len(nums)
        need_swaps = {nums[i] for i in range(n) if nums[i] != i}
        
        def can_sort_with_k(k):
            nonlocal need_swaps
            nodes = set()
            for i in range(n):
                for j in range(i+1, n):
                    if nums[i] & nums[j] == k:
                        nodes.add(nums[i])
                        nodes.add(nums[j])
            if not need_swaps.difference(nodes):
                return True
            return False
        
        for k in reversed(range(n-1)):
            if can_sort_with_k(k):
                return k
        return 0

# Group values as all values in one group that satisfy (x & y == k, for x, y in 0 ... n-1 and x != y)
class Solution2:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
            
        def can_sort_with_k(k):
            parent = list(range(n))
            def find(x):
                nonlocal parent
                while x != parent[x]:
                    x = parent[x]
                return x
            
            def union(x, y):
                nonlocal parent
                rx, ry = find(x), find(y)
                if rx != ry:
                    parent[ry] = rx
                    
            for i in range(n):
                for j in range(i+1, n):
                    if i & j == k:
                        union(i, j)
            print("DEBUG: ", parent)
            for i in range(n):
                if nums[i] == i:
                    continue
                ## This means that if num at pos i in the same group of i
                # (because i is supposed at pos i after sorted, and i is on somewhere else now)
                # assume nums[x]
                # that means nums[x] and nums[i] can be swapped with k
                if find(nums[i]) != find(i):
                    return False
            return True
        # search k by bit add
        k = 0
        # already sorted
        if all([nums[i] == i for i in range(n)]):
            return 0
        bits = math.ceil(math.log(n-1, 2))
        for b in range(bits, -1, -1):
            candidate = k | (1 << b)
            if can_sort_with_k(candidate):
                k = candidate
        return k
      
        
if __name__ == '__main__':
    nums = [1, 0]
    s = Solution()
    r = s.sortPermutation(nums)
    print(r)
    s2 = Solution2()
    r2 = s2.sortPermutation(nums)
    print(r2)