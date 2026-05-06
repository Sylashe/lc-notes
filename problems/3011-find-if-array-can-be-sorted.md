# 3011. Find if Array Can Be Sorted

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Bit Manipulation` `Sorting`

## Problem

> You are given a 0-indexed array of positive integers nums.  In one operation, you can swap any two adjacent elements if they have the same number of set bits. You are allowed to do this operation any number of times (including zero).  Return true if you can sort the array in ascending order, else return false.    Example 1:   Input: nums = [8,4,2,30,15] Output: true Explanation: Let's look at the...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        pre_max = 0
        while i < n:
            current = nums[i].bit_count()
            mx = nums[i]
            while i < n and nums[i].bit_count() == current:
                if nums[i] < pre_max:
                    return False
                mx = max(mx, nums[i])
                i += 1
            pre_max = mx
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3011 Find if Array Can Be Sorted -->
