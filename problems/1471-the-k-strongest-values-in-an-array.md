# 1471. The k Strongest Values in an Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Sorting`

## Problem

> Given an array of integers arr and an integer k.  A value arr[i] is said to be stronger than a value arr[j] if |arr[i] - m| > |arr[j] - m| where m is the centre of the array. If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j] if arr[i] > arr[j].  Return a list of the strongest k values in the array. Return the answer in any arbitrary order.  The centre is the middle va...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        l = 0
        r = len(arr) - 1
        m = arr[r//2]
        while r - l + 1 > len(arr) - k:
            if abs(arr[l] - m) <= abs(arr[r] - m):
                r -= 1
            else:
                l += 1
        return arr[:l] + arr[r+1:]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1471 The k Strongest Values in an Array -->
