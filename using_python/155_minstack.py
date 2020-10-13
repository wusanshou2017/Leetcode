class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_res = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.stack_res:
            if x <= self.stack_res[-1]:
                self.stack_res.append(x)
        else:
            self.stack_res.append(x)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.stack_res[-1]:
            self.stack_res.pop()
        else:
            return

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return

    def getMin(self) -> int:
        if self.stack_res:
            return self.stack_res[-1]
        else:
            return


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
#
#
# ["MinStack","push","push","push","getMin","pop","getMin"]
# [[],[0],[1],[0],[],[],[]]
# [null,null,null,null,0,null,0]
