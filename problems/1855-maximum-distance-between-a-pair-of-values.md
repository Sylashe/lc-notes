# 1855. Maximum Distance Between a Pair of Values

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Binary Search`

## Problem

> You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.  A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.  Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.  An array arr is non-increasing if arr[i-1] >= a...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        ans = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1855 Maximum Distance Between a Pair of Values -->
