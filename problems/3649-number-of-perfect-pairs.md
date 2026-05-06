# 3649. Number of Perfect Pairs

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Math` `Two Pointers` `Sorting`

## Problem

> You are given an integer array nums.  A pair of indices (i, j) is called perfect if the following conditions are satisfied:   	i < j 	Let a = nums[i], b = nums[j]. Then: 	 		min(|a - b|, |a + b|) <= min(|a|, |b|) 		max(|a - b|, |a + b|) >= max(|a|, |b|) 	 	   Return the number of distinct perfect pairs.  Note: The absolute value |x| refers to the non-negative value of x.    Example 1:   Input: num...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            nums[i] = abs(x)
        nums.sort()
        ans = 0
        l = 0
        for r in range(1, len(nums)):
            while 2 * nums[l] < nums[r]:
                l += 1
            ans += r - l
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3649 Number of Perfect Pairs -->
