# 2529. Maximum Count of Positive Integer and Negative Integer

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Binary Search` `Counting`

## Problem

> Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.   	In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.   Note that 0 is neither positive nor negative.    Example 1:   Input: nums = [-2,-1,-1,1,2,3] Outp...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid - 1
        neg = l
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid - 1
        pos = n - l
        return max(neg, pos)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2529 Maximum Count of Positive Integer and Negative Integer -->
