# 1588. Sum of All Odd Length Subarrays

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Math` `Prefix Sum`

## Problem

> Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.  A subarray is a contiguous subsequence of the array.    Example 1:   Input: arr = [1,4,2,5,3] Output: 58 Explanation: The odd-length subarrays of arr and their sums are: [1] = 1 [4] = 4 [2] = 2 [5] = 5 [3] = 3 [1,4,2] = 7 [4,2,5] = 11 [2,5,3] = 10 [1,4,2,5,3] = 15 If we add all these together we g...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i = 0
        ans = 0
        n = len(arr)
        s = [0] * (len(arr) + 1)
        for i, num in enumerate(arr):
            s[i + 1] = num + s[i]
        for i in range(n):
            for j in range(i, n):
                if ((j - i + 1) % 2) == 1:
                    ans += s[j + 1] - s[i]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1588 Sum of All Odd Length Subarrays -->
