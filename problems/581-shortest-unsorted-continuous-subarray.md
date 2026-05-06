# 581. Shortest Unsorted Continuous Subarray

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Stack` `Greedy` `Sorting` `Monotonic Stack`

## Problem

> Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.  Return the shortest such subarray and output its length.    Example 1:   Input: nums = [2,6,4,8,10,9,15] Output: 5 Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole arr...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        r = n - 1
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1
        ans = r
        l = 0
        if r == 0:
            return 0
        max_r = max(nums[:r+1])
        while r < n - 1 and nums[r + 1] < max_r:
            r += 1
        while l == 0 or nums[l] >= nums[l - 1]:
            l += 1
        min_l = min(nums[l:])
        while l > 0 and nums[l - 1] > min_l:
            l -= 1
        ans = r - l + 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #581 Shortest Unsorted Continuous Subarray -->
