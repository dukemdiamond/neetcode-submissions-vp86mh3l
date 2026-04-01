class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in freq_s:
                freq_s[s[i]] = 1
            if t[i] not in freq_t:
                freq_t[t[i]] = 1
            freq_s[s[i]] += 1
            freq_t[t[i]] += 1
        
        return freq_s == freq_t
            