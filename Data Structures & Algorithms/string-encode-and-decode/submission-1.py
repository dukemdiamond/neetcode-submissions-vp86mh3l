class Solution:
    
    def encode(self, strs: List[str]) -> str:
        # For encode:
        # Make a blank encode list, separating strings with a separator 
        # This will distinguish what is hwat

        encode = []
        # Iterate through strs to make a together-ed list
        for s in strs:
            encode.append(f"{len(s)}#{s}")
        return ''.join(encode)
    
    def decode(self, s:str) -> List[str]:
        # We want to decode a string back into a list of strings. 
        # We can move through the string that is encoded, one at a time
        res = []
        i = 0
        # Find the separator '#'
        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1
            # once we find, we can get the length
            length = int(s[i:j])

            word = s[(j + 1) : (j + 1 + length)]
            res.append(word)

            # then, move the pointer to the next encoded word
            i = j + 1 + length
        return res