class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for ch in s:
            if ch != ' ' and ch.isalnum():
                chars.append(ch.lower())
            
        t = "".join(chars)
        print(t)
        return t == t[::-1]