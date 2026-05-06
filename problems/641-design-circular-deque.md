# 641. Design Circular Deque

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Linked List` `Design` `Queue`

## Problem

> Design your implementation of the circular double-ended queue (deque).  Implement the MyCircularDeque class:   	MyCircularDeque(int k) Initializes the deque with a maximum size of k. 	boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise. 	boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is suc...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.arr = k * [0]
        self.size = 0
        self.front = k - 1
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        self.arr[self.front] = value
        self.front = (self.front - 1) % self.k
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.front = (self.front + 1) % self.k
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.rear = (self.rear - 1) % self.k
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.front + 1) % self.k]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1) % self.k]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #641 Design Circular Deque -->
