class Solution:
    def isValid(self, s: str) -> bool:
        # Think of this in terms of a stack
        # ([])
        # Iterate through our array. If it's an open bracket,
        # Then we want to pop the end of the array. The popped char must be the close bracket; or else False.
        stack = []
        closeToOpen = {'}': '{', ']': '[', ')': '('}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False