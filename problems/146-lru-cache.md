# 146. LRU Cache

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `Linked List` `Design` `Doubly-Linked List`

## Problem

> Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.  Implement the LRUCache class:   	LRUCache(int capacity) Initialize the LRU cache with positive size capacity. 	int get(int key) Return the value of the key if the key exists, otherwise return -1. 	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair t...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last = False)
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last = False)
        if len(self.cache) > self.capacity:
            self.cache.popitem()



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #146 LRU Cache -->
