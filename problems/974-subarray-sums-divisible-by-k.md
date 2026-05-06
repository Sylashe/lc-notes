# 974. Subarray Sums Divisible by K

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Prefix Sum`

## Problem

> Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.  A subarray is a contiguous part of an array.    Example 1:   Input: nums = [4,5,0,-2,-3,1], k = 5 Output: 7 Explanation: There are 7 subarrays with a sum divisible by k = 5: [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]   Example 2:   Input: nums =...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = [0] * k
        cnt[0] = 1
        pre_s = 0
        r = 0
        for num in nums:
            r = (r + num) % k
            ans += cnt[r]
            cnt[r] += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #974 Subarray Sums Divisible by K -->
