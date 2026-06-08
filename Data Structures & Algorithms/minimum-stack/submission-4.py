class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # every element in the stack should know about its minimum at that point

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if self.minStack[-1] < val:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]