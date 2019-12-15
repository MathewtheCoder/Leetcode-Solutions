class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(self.getMin(), x)))

    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return float('inf')


test = MinStack()
test.push(-2)
test.push(0)
test.push(-3)
print(test.getMin())
print(test.pop())
print(test.top())
print(test.getMin())
