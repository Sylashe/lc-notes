# 1004. Max Consecutive Ones III

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search` `Sliding Window` `Prefix Sum`

## Problem

> Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.    Example 1:   Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 Output: 6 Explanation: [1,1,1,0,0,1,1,1,1,1,1] Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.  Example 2:   Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3 Output:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        s = 0
        ans = 0
        for right, num in enumerate(nums):
            s += 1 - num
            while s > k:
                if left < len(nums) and nums[left] == 0:
                    s -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1004 Max Consecutive Ones III -->
