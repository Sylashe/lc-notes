# 3467. Transform Array by Parity

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Sorting` `Counting`

## Problem

> You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:   	Replace each even number with 0. 	Replace each odd numbers with 1. 	Sort the modified array in non-decreasing order.   Return the resulting array after performing these operations.    Example 1:   Input: nums = [4,3,2,1]  Output: [0,0,1,1]  Explanation:   	Replace the even nu...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        cnt1 = sum(x%2 for x in nums)
        cnt0 = len(nums) - cnt1
        return [0] * cnt0 + [1] * cnt1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3467 Transform Array by Parity -->
