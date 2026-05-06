# 34. Find First and Last Position of Element in Sorted Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search`

## Problem

> Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.  If target is not found in the array, return [-1, -1].  You must write an algorithm with O(log n) runtime complexity.    Example 1: Input: nums = [5,7,7,8,8,10], target = 8 Output: [3,4] Example 2: Input: nums = [5,7,7,8,8,10], target = 6 Output: [-1,-1] Example 3: Input:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums, target):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l)//2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        if lower_bound(nums, target) == len(nums) or nums[lower_bound(nums, target)] != target:
            return [-1, -1]
        return [lower_bound(nums, target), lower_bound(nums, target + 1) - 1]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #34 Find First and Last Position of Element in Sorted Array -->
