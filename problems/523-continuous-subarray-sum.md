# 523. Continuous Subarray Sum

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Math` `Prefix Sum`

## Problem

> Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.  A good subarray is a subarray where:   	its length is at least two, and 	the sum of the elements of the subarray is a multiple of k.   Note that:   	A subarray is a contiguous part of the array. 	An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a m...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ans = 0
        pre_s = 0
        cnt = defaultdict(int)
        cnt[0] = -1
        for i, num in enumerate(nums):
            pre_s += num
            r = pre_s % k
            if r in cnt:
                if i - cnt[r] >= 2:
                    return True
            else:
                cnt[r] = i
        return False
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #523 Continuous Subarray Sum -->
