# 3131. Find the Integer Added to Array I

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array`

## Problem

> You are given two arrays of equal length, nums1 and nums2.  Each element in nums1 has been increased (or decreased in the case of negative) by an integer, represented by the variable x.  As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.  Return the integer x.    Example 1:   Input: nums1 = [2,6,4], nums2 = [9,7...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3131 Find the Integer Added to Array I -->
