# 2348. Number of Zero-Filled Subarrays

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Math`

## Problem

> Given an integer array nums, return the number of subarrays filled with 0.  A subarray is a contiguous non-empty sequence of elements within an array.    Example 1:   Input: nums = [1,3,0,0,2,0,0,4] Output: 6 Explanation:  There are 4 occurrences of [0] as a subarray. There are 2 occurrences of [0,0] as a subarray. There is no occurrence of a subarray with a size more than 2 filled with 0. Therefo...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        for num in nums:
            if num == 0:
                cnt += 1
                ans += cnt
            else:
                cnt = 0
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2348 Number of Zero-Filled Subarrays -->
