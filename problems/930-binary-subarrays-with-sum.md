# 930. Binary Subarrays With Sum

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Sliding Window` `Prefix Sum`

## Problem

> Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.  A subarray is a contiguous part of the array.    Example 1:   Input: nums = [1,0,1,0,1], goal = 2 Output: 4 Explanation: The 4 subarrays are bolded and underlined below: [1,0,1,0,1] [1,0,1,0,1] [1,0,1,0,1] [1,0,1,0,1]   Example 2:   Input: nums = [0,0,0,0,0], goal = 0 Output: 15     Constraint...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def f(k: int) -> int:
            if k < 0:
                return 0
            s = 0
            cnt = 0
            l = 0
            for r, num in enumerate(nums):
                s += num
                while s > k:
                    s -= nums[l]
                    l += 1
                cnt += r - l + 1
            return cnt
        return f(goal) - f(goal - 1)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #930 Binary Subarrays With Sum -->
