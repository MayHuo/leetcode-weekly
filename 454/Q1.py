
class Solution:
    def generateTag(self, caption: str) -> str:
        output = "#"
        n = len(caption)
        l, r = 0,  0
        caption.strip()
        
        while l <= r < n:
            while l < n and caption[l] == " ":
                l += 1
            continue
            while r < n and caption[r] != " ":
                r += 1
            if l == 0:
                output += caption[l].lower()
            else:
                output += caption[l].upper()
            output += caption[l+1:r]
            if length >= 100:
                break
            l = r+1
            r += 1
        return output[:100]


sol = Solution()
caption = "     "

r = sol.generateTag(caption)
print(r)
