# 4. Median of Two Sorted Arrays

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Array` `Binary Search` `Divide and Conquer`

## Problem

> Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.  The overall run time complexity should be O(log (m+n)).    Example 1:   Input: nums1 = [1,3], nums2 = [2] Output: 2.00000 Explanation: merged array = [1,2,3] and median is 2.   Example 2:   Input: nums1 = [1,2], nums2 = [3,4] Output: 2.50000 Explanation: merged array = [1,2,3,4] and m...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        return nums[len(nums)//2] if len(nums) % 2 == 1 else (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #4 Median of Two Sorted Arrays -->
