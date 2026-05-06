# 1537. Get the Maximum Score

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Array` `Two Pointers` `Dynamic Programming` `Greedy`

## Problem

> You are given two sorted arrays of distinct integers nums1 and nums2.  A valid path is defined as follows:   	Choose array nums1 or nums2 to traverse (from index-0). 	Traverse the current array from left to right. 	If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).   The...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        sum1 = sum2 = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums2[j] < nums1[i]:
                sum2 += nums2[j]
                j += 1
            else:
                 sum1 = sum2 = max(sum1, sum2) + nums1[i]
                 i += 1
                 j += 1
        sum1 += sum(nums1[i:])
        sum2 += sum(nums2[j:])
        return max(sum1, sum2) % (10 ** 9 + 7)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1537 Get the Maximum Score -->
