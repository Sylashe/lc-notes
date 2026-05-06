# 88. Merge Sorted Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers` `Sorting`

## Problem

> You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.  Merge nums1 and nums2 into a single array sorted in non-decreasing order.  The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a lengt...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        idx = m + n - 1
        while j >= 0:
            if i >=0 and nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #88 Merge Sorted Array -->
