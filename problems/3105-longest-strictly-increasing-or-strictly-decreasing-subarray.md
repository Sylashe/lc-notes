# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array`

## Problem

> You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.    Example 1:   Input: nums = [1,4,3,3,2]  Output: 2  Explanation:  The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].  The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].  Hence, w...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        i = 0
        n = len(nums)
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                i += 1
                continue
            d = nums[i + 1] > nums[i]
            start_i = i
            while i < n - 1 and nums[i] != nums[i + 1] and (nums[i + 1] > nums[i]) == d:
                i += 1
            ans = max(ans, i - start_i + 1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3105 Longest Strictly Increasing or Strictly Decreasing Subarray -->
