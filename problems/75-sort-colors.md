# 75. Sort Colors

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Sorting`

## Problem

> Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.  We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.  You must solve this problem without using the library's sort function.    Example 1:   Input: nums = [2,0,2,1,1,0] Outpu...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
       p0 = 0
       p1 = 0
       for i,x in enumerate(nums):
        nums[i] = 2
        if x <= 1:
            nums[p1] = 1
            p1 += 1
        if x == 0:
            nums[p0] = 0
            p0 += 1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #75 Sort Colors -->
