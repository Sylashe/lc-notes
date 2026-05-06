# 3132. Find the Integer Added to Array II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Sorting` `Enumeration`

## Problem

> You are given two integer arrays nums1 and nums2.  From nums1 two elements have been removed, and all other elements have been increased (or decreased in the case of negative) by an integer, represented by the variable x.  As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.  Return the minimum possible integer x...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int: 
        nums1.sort()
        nums2.sort()
        for i in range(2, 0, -1):
            x = nums2[0] - nums1[i]
            j = 0
            for num in nums1[i:]:
                if num + x == nums2[j]:
                    j += 1
                if j == len(nums2):
                    return x
        return nums2[0] - nums1[0]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3132 Find the Integer Added to Array II -->
