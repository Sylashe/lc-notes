# 81. Search in Rotated Sorted Array II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search`

## Problem

> There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).  Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and be...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return True
            if nums[l] <= nums[mid]:
                if nums[l] == nums[mid]:
                    l += 1
                    continue
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #81 Search in Rotated Sorted Array II -->
