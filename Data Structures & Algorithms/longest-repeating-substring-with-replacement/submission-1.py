class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        maxf = 0
        count = {}
        
        for r in range(len(s)):
            # 1. include s[r] in the window
            count[s[r]] = 1 + count.get(s[r], 0)
            # 2. check if the window is invalid
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

