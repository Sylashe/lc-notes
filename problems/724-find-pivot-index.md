# 724. Find Pivot Index

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Prefix Sum`

## Problem

> Given an array of integers nums, calculate the pivot index of this array.  The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.  If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the ar...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_fix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            pre_fix[i + 1] = pre_fix[i] + num
        for i in range(1, len(pre_fix)):
            if pre_fix[i - 1] == pre_fix[len(pre_fix) - 1] - pre_fix[i]:
                return i - 1
        return -1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #724 Find Pivot Index -->
