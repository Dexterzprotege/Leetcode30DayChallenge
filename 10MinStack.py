"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 
Constraints: Methods pop, top and getMin operations will always be called on non-empty stacks.
"""
class MinStack:
    def __init__(self):
        self.s = []
        self.m = None
    def push(self, x):
        if not self.s:
            self.s.append(x)
            self.m = x
            return 
        if x < self.m:
            self.s.append(2*x-self.m)
            self.m = x
            return
        self.s.append(x)
    def pop(self):
        y = self.s[-1]
        self.s.pop()
        if y < self.m:
            self.m = 2*self.m -y

    def top(self):
        y = self.s[-1]
        if y < self.m:
            return self.m
        return y
        
    def getMin(self):
        return self.m
