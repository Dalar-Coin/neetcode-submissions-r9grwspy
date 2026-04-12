class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            sortedS = ''.join(sorted(s))
            d[sortedS] = d.get(sortedS, []) + [s]
        return list(d.values())