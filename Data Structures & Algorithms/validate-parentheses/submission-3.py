class Solution:
    def isValid(self, s: str) -> bool:
        # Think of this in terms of a stack
        # ([])
        # Iterate through our array. If it's an open bracket,
        # Then we want to pop the end of the array. The popped char must be the close bracket; or else False.
        stack = []
        pr = {'(': ')', '{': '}', '[': ']'}
        for ch in s:

            if ch in pr:
                stack.append(ch)
                
            else:

                if not stack:
                    return False
                popped = stack.pop()

                if pr[popped] != ch:
                    return False

        return len(stack) == 0
    




        