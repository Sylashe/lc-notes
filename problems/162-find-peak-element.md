# 162. Find Peak Element

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search`

## Problem

> A peak element is an element that is strictly greater than its neighbors.  Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.  You may imagine that nums[-1] = nums[n] = -&infin;. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #162 Find Peak Element -->
