class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            key = tuple(sorted(s)) # tuple is needed to hash
            if key not in hm:
                hm[key] = [] # initialize hash map if first run

            hm[key].append(s) # add the string

        return hm.values() # return the values
        
        