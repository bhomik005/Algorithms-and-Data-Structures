class Stack:
    def __init__(self):
        self.stack = []

    # O(1) time
    def push(self, n):
        self.stack.append(n)
    
    # O(1) time
    def pop(self):
        return self.stack.pop()
    
    # O(1) time
    def peek(self):
        return self.stack[-1]