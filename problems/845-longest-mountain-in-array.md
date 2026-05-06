# 845. Longest Mountain in Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Dynamic Programming` `Enumeration`

## Problem

> You may recall that an array arr is a mountain array if and only if:   	arr.length >= 3 	There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that: 	 		arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 		arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 	 	   Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subar...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        i = 0
        if n < 3:
            return ans
        while i < n:
            if i < n - 1 and arr[i] < arr[i + 1]:
                start_i = i
                while i < n - 1 and arr[i] < arr[i + 1]:
                    i += 1
                peak = i
                while i < n - 1 and arr[i] > arr[i + 1]:
                    i += 1
                if i > peak and i - start_i + 1 >= 3:
                    ans = max(ans, i - start_i + 1) 
            else:
                i += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #845 Longest Mountain in Array -->
