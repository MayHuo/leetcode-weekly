
class Solution:
    def processStr(self, s: str) -> str:
        result = ''
        for c in s:
            if c.islower():
                result += c
            elif c == '*' and result:
                result = result[:-1]
            elif c == '#':
                result += result
            elif c == '%':
                result = ''.join([result[i] for i in range(len(result)-1, -1, -1)])
        return result
    
s = "a#b%*"
r = processStr(s)
print(r)

