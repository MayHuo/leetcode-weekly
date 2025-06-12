#3567. Minimum Absolute Difference in Sliding Submatrix
# Given an mxn matrix and in integer k
# For every contiguous kxk submatrix, compute the minimum absolute difference
# between any two distinct values within that submatrix

from typing import List
import math

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n-k+1) for _ in range(m-k+1)]
        if k == 1: return ans
        
        for i in range(m-k+1):
            for j in range(n-k+1):
                # compute submatrix  matrix[i:i+k][j:j+k]
                # maybe chained submatrix to a new list is easier to indexes, and how?
                sub = [0] * (k*k)
                for a in range(i, i+k):
                    for b in range(j, j+k):
                        idx = (a-i)*k + (b-j)
                        sub[idx] = grid[a][b]
                # print(sub)
                mini = math.inf
                for x in range(len(sub)):
                    for y in range(x+1, len(sub)):
                        if sub[x] == sub[y]:
                            continue
                        mini = min(abs(sub[x] - sub[y]), mini)
                if mini == math.inf:
                    mini = 0
                ans[i][j] = mini
                print("******", i, j)

        return ans


# class Solution:
#     def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
#         m = len(grid)
#         n = len(grid[0])
#         ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
#         if k == 1: return ans
#
#         for i in range(m - k + 1):
#             for j in range(n - k + 1):
#                 # submatrix grid[i:i+k][j:j+k]
#                 # flatten subMatrix as list
#                 subM = [0] * (k * k)
#                 for r in range(i, i + k):
#                     for c in range(j, j + k):
#                         idx = (r - i) * k + (c - j)
#                         subM[idx] = grid[r][c]
#                 print(subM)
#                 mini = math.inf
#                 for x in range(len(subM)):
#                     for y in range(x + 1, len(subM)):
#                         if subM[x] == subM[y]:
#                             continue
#                         mini = min(abs(subM[x] - subM[y]), mini)
#                 ans[i][j] = mini
#         return ans
      

if __name__ == '__main__':
    grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    k = 5
    sol = Solution()
    ans = sol.minAbsDiff(grid, k)
    print(ans)