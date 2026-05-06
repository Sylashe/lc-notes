# 3708. Longest Fibonacci Subarray

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array`

## Problem

> You are given an array of positive integers nums.  A Fibonacci array is a contiguous sequence whose third and subsequent terms each equal the sum of the two preceding terms.  Return the length of the longest Fibonacci subarray in nums.  Note: Subarrays of length 1 or 2 are always Fibonacci.    Example 1:   Input: nums = [1,1,1,1,2,3,5,1]  Output: 5  Explanation:  The longest Fibonacci subarray is...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = 2
        ans = 0
        for i, num in enumerate(nums):
            if i >= 2 and nums[i] == nums[i - 1] + nums[i - 2]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 2
        ans = max(ans, cnt)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3708 Longest Fibonacci Subarray -->
