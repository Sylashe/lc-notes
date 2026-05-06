# 35. Search Insert Position

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Binary Search`

## Problem

> Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.  You must write an algorithm with O(log n) runtime complexity.    Example 1:   Input: nums = [1,3,5,6], target = 5 Output: 2   Example 2:   Input: nums = [1,3,5,6], target = 2 Output: 1   Example 3:   Input: nums = [1,3,5,6]...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #35 Search Insert Position -->
