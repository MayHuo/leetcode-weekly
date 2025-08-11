# Integer array weight of length n, for n parcels
# A shipment is defined as a contiguous subarray of parcels
# A balance shipment is satisfied the condition:
# the weight of last parcel is strictly less the maximum weight among all parcels in that shipment

from typing import List

class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        # greedy?
        result = 0
        n = len(weight)
        maximum = 0
        for last in range(1, n):
            if weight[last] < weight[maximum]:
                result += 1
                maximum = last + 1
                continue
            maximum = last
        return result

s = Solution()
weight = [5, 2, 1]
r = s.maxBalancedShipments(weight)
print(r)
            
            