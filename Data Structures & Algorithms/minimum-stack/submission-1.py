class MinStack:

    def __init__(self):
        self.stack = []
        self.min_indexs = []
        

    def push(self, val: int) -> None:
        if self.stack:
            current_min = self.getMin()
            if val <= current_min:
                new_min_index = len(self.stack)
                self.min_indexs.append(new_min_index)
            else:
                self.min_indexs.append(self.min_indexs[-1])
        else:
            self.min_indexs.append(0)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.min_indexs.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        min_index = self.min_indexs[-1]
        minimum = self.stack[min_index]
        return minimum

        
