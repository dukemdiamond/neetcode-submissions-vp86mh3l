class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(c.lower() for c in s if c.isalnum())
        i = len(clean_text) - 1
        j = 0
        while j < i:
            if clean_text[j] == clean_text[i]:
                j += 1
                i -=1
            else:
                return False

        return True


        