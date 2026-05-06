# 3914. Minimum Operations to Make Array Non Decreasing

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** 

## Problem

> You are given an integer array nums of length n.  In one operation, you may choose any subarray nums[l..r] and increase each element in that subarray by x, where x is any positive integer.  Return the minimum possible sum of the values of x across all operations required to make the array non-decreasing.  An array is non-decreasing if nums[i] <= nums[i + 1] for all 0 <= i < n - 1.    Example 1:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if nums[i] < nums[i - 1]:
                ans += nums[i - 1] - nums[i]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3914 Minimum Operations to Make Array Non Decreasing -->
