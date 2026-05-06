# 209. Minimum Size Subarray Sum

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search` `Sliding Window` `Prefix Sum`

## Problem

> Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.    Example 1:   Input: target = 7, nums = [2,3,1,2,4,3] Output: 2 Explanation: The subarray [4,3] has the minimal length under the problem constraint.   Example 2:   Input: target = 4, nums = [1...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        cnt = 0
        l = 0
        for r, x in enumerate(nums):
            cnt += x
            while cnt >= target:
                ans = min(ans, r - l + 1)
                cnt -= nums[l]
                l += 1
        return 0 if ans == float('inf') else ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #209 Minimum Size Subarray Sum -->
