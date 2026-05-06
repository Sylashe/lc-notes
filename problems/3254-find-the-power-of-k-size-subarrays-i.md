# 3254. Find the Power of K-Size Subarrays I

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sliding Window`

## Problem

> You are given an array of integers nums of length n and a positive integer k.  The power of an array is defined as:   	Its maximum element if all of its elements are consecutive and sorted in ascending order. 	-1 otherwise.   You need to find the power of all subarrays of nums of size k.  Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].    E...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        cnt = 0
        for i, num in enumerate(nums):
            if i == 0 or nums[i - 1] + 1 == num:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ans[i - k + 1] = num
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3254 Find the Power of K-Size Subarrays I -->
