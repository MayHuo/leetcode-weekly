from typing import List
import math

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        
        n = len(complexity)
        iterator = iter(complexity)
        complex, label = next(iterator), 0
        for i, cur in enumerate(iterator, start=1):
            if (cur < complex) or (cur == complex and i > 1):
                return 0
        factorial = 1
        for i in range(n):
            factorial *= i
        return factorial % (10**9+7)
            
    
    
if __name__ == '__main__':
    complexity = [3, 3, 3, 4,4 ,4]
    solution = Solution()
    r = solution.countPermutations(complexity)
    print(r)