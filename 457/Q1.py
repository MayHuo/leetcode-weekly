import re
from typing import List
from collections import OrderedDict

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        code_pattern = re.compile(r'[a-zA-Z0-9_]+')
        n = len(code)
        result = OrderedDict({
            'electronics': [],
            'grocery': [],
            'pharmacy': [],
            'restaurant': []
        })
        for i in range(n):
            if not re.match(code_pattern, code[i]):
                print(f"Invalid code: {code[i]}")
                continue
            if not isActive[i]:
                continue
            container = result.get(businessLine[i], None)
            if container is None:
                continue
            container.append(code[i])
        
        actives = []
        for k in result:
            result[k].sort()
            actives.extend(result[k])
        
        return actives

code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
businessLine = ["grocery","electronics","invalid"]
isActive = [False,True,True]

s = Solution()
r = s.validateCoupons(code, businessLine, isActive)
print(r)

        
        
