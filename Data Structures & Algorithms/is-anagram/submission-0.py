class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        for ch in s:
            if not hm1.get(ch):
                hm1[ch] = 1

            if (hm1[ch]):
                hm1[ch] += 1
        hm2 = {}
        for chi in t:
            if not hm2.get(chi):
                hm2[chi] = 1

            if (hm2[chi]):
                hm2[chi] += 1

        return hm1 == hm2



        