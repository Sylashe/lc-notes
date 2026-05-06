# 53. Maximum Subarray

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Divide and Conquer` `Dynamic Programming`

## Problem

> Given an integer array nums, find the subarray with the largest sum, and return its sum.    Example 1:   Input: nums = [-2,1,-3,4,-1,2,1,-5,4] Output: 6 Explanation: The subarray [4,-1,2,1] has the largest sum 6.   Example 2:   Input: nums = [1] Output: 1 Explanation: The subarray [1] has the largest sum 1.   Example 3:   Input: nums = [5,4,-1,7,8] Output: 23 Explanation: The subarray [5,4,-1,7,8]...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cnt = 0
        ans = nums[0]
        for num in nums:
            if cnt < 0:
                cnt =0
            cnt += num
            ans = max(ans, cnt)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #53 Maximum Subarray -->
