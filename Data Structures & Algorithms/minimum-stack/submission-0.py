class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] # this is effectively peek

    def getMin(self) -> int:
        if self.stack:
            stack_min = self.stack[0]
            for s in self.stack:
                if s < stack_min:
                    stack_min = s
            return stack_min
        return 0 
        
