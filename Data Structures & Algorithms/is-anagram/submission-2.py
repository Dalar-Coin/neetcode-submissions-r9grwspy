class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        Sstring = {}
        Tstring = {}

        for i in range(len(s)):
            Sstring[s[i]] = 1 + Sstring.get(s[i], 0)
            Tstring[t[i]] = 1 + Tstring.get(t[i], 0)
        
        return Sstring == Tstring