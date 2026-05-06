# 410. Split Array Largest Sum

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Array` `Binary Search` `Dynamic Programming` `Greedy` `Prefix Sum`

## Problem

> Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.  Return the minimized largest sum of the split.  A subarray is a contiguous part of the array.    Example 1:   Input: nums = [7,2,5,10,8], k = 2 Output: 18 Explanation: There are four ways to split nums into two subarrays. The best way is to split it into [7,2...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mx):
            cnt = 1
            s = 0
            for i, num in enumerate(nums):
                if s + num <= mx:
                    s += num
                else:
                    cnt += 1
                    s = num
            return cnt <= k
        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = l + (r - l)//2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #410 Split Array Largest Sum -->
