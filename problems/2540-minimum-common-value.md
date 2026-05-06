# 2540. Minimum Common Value

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Two Pointers` `Binary Search`

## Problem

> Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.  Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.    Example 1:   Input: nums1 = [1,2,3], nums2 = [2,4] Output: 2 Explanation: The smalle...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l = 0
        r = 0
        ans = -1
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                return nums1[l]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2540 Minimum Common Value -->
