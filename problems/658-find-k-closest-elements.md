# 658. Find K Closest Elements

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Binary Search` `Sliding Window` `Sorting` `Heap (Priority Queue)`

## Problem

> Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.  An integer a is closer to x than an integer b if:   	|a - x| < |b - x|, or 	|a - x| == |b - x| and a < b     Example 1:   Input: arr = [1,2,3,4,5], k = 4, x = 3  Output: [1,2,3,4]   Example 2:   Input: arr = [1,1,2,3,4,5], k = 4, x = -1  Out...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        while r - l + 1 > k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #658 Find K Closest Elements -->
