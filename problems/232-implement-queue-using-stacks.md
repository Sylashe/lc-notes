# 232. Implement Queue using Stacks

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Stack` `Design` `Queue`

## Problem

> Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).  Implement the MyQueue class:   	void push(int x) Pushes element x to the back of the queue. 	int pop() Removes the element from the front of the queue and returns it. 	int peek() Returns the element at the front of the queue. 	bo...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def push(self, x: int) -> None:
        self.in_stack.append(x)
    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
    def peek(self) -> int:
        val = self.pop()
        self.out_stack.append(val)
        return val
        return self.out_stack[-1]
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #232 Implement Queue using Stacks -->
