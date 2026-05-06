# 1089. Duplicate Zeros

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers`

## Problem

> Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.  Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.    Example 1:   Input: arr = [1,0,2,3,0,4,5,0] Output: [1,0,0,2,3,0,0,4] Explanation: After calling your function, the...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_cnt = Counter(arr)[0]
        k = len(arr) + zero_cnt - 1
        j = len(arr) - 1
        while j >= 0:
            if k < len(arr):
                arr[k] = arr[j]
            if arr[j] == 0:
                k -= 1
                if k < len(arr):
                    arr[k] = 0
            k -= 1
            j -= 1
        return arr
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1089 Duplicate Zeros -->
