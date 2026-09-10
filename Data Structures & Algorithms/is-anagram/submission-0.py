class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        Hmap1 = {}
        Hmap2 = {}

        for i in range(len(s)):
            Hmap1[s[i]] = 1 + Hmap1.get(s[i], 0)
            Hmap2[t[i]] = 1 + Hmap2.get(t[i], 0)

        for c in Hmap1:
            if Hmap1[c] != Hmap2.get(c, 0):
                return False
        return True