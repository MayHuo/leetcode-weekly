# x = the number of currently active elements
# total = total activation value
# limit[j] < actives, permanently inactive
# Return the maximum total you can obtain by choosing the activation order optimally

from typing import List
import heapq

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        n = len(value)
        # item = (limit[i], -value[i])
        permanent_inactive = [0] * n
        heap = [[limit[i], -value[i], i] for i in range(n)]
        heapq.heapify(heap)
        total = 0
        x = 0
        while heap:
            lim, v, i = heapq.heappop(heap)
            if permanent_inactive[i]:
                continue
            if x < lim:
                total += -v
                x += 1
                # for j in range(n):
                #     if limit[j] <= x:
                #         permanent_inactive[j] = 1
        return total
        
if __name__ == '__main__':
    value = [4, 1, 5, 2]
    limit = [3, 3, 2, 3]
    solution = Solution()
    ret = solution.maxTotal(value, limit)
    print(ret)
        

