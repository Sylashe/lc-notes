# 153. Find Minimum in Rotated Sorted Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search`

## Problem

> Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:   	[4,5,6,7,0,1,2] if it was rotated 4 times. 	[0,1,2,4,5,6,7] if it was rotated 7 times.   Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].  Given the sorted rotated ar...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #153 Find Minimum in Rotated Sorted Array -->
