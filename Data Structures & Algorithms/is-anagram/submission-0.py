class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Anagrams
        mapS = {}
        for ch in s:
            mapS[ch] = mapS.get(ch, 0) + 1

        mapT = {}
        for ch in t:
            mapT[ch] = mapT.get(ch, 0) + 1

        # Checks
        return mapS == mapT
        