# 3424. Minimum Cost to Make Arrays Identical

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Greedy` `Sorting`

## Problem

> You are given two integer arrays arr and brr of length n, and an integer k. You can perform the following operations on arr any number of times:   	Split arr into any number of contiguous subarrays and rearrange these subarrays in any order. This operation has a fixed cost of k. 	 	Choose any element in arr and add or subtract a positive integer x to it. The cost of this operation is x. 	   Return...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        ans_1 = 0
        n = len(brr)
        for i in range(n):
            ans_1 += abs(arr[i] - brr[i])
        arr.sort()
        brr.sort()
        ans_2 = k
        for i in range(n):
            ans_2 += abs(arr[i] - brr[i])
        return min(ans_1,ans_2)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3424 Minimum Cost to Make Arrays Identical -->
