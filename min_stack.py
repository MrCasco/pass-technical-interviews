"""
KEY: Key here is to keep track of the minimum value among the whole
stack by saving it on a tuple with the value example:
stack = [(1, 1), (2, 1), (3, 1), (-1, -1), (0, -1)]

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

"""

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: self.stack.append((val, val))
        else: self.stack.append((val, min(self.stack[-1][1], val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
