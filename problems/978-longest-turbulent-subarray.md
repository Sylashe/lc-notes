# 978. Longest Turbulent Subarray

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Dynamic Programming` `Sliding Window`

## Problem

> Given an integer array arr, return the length of a maximum size turbulent subarray of arr.  A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.  More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:   	For i <= k < j:  	 		arr[k] > arr[k + 1] when k is odd, and 		arr[k] < arr[k + 1] when k...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 1
        ans = cur_len = 1
        prev_cmp = 0
        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                cur_cmp = 0
            elif arr[i] > arr[i - 1]:
                cur_cmp = 1
            else:
                cur_cmp = -1
            if cur_cmp == 0:
                cur_len = 1
            elif cur_cmp == -prev_cmp:
                cur_len += 1
            else:
                cur_len = 2
            ans = max(ans, cur_len)
            prev_cmp = cur_cmp
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #978 Longest Turbulent Subarray -->
