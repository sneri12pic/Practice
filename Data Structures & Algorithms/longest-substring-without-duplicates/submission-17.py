class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxL = 0 
        seen = set()

        for r in range(len(s)):
            char = s[r]
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            maxL = max(maxL, r - l + 1)
        return maxL

                

