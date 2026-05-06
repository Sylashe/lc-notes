# 2799. Count Complete Subarrays in an Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Sliding Window`

## Problem

> You are given an array nums consisting of positive integers.  We call a subarray of an array complete if the following condition is satisfied:   	The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.   Return the number of complete subarrays.  A subarray is a contiguous non-empty part of an array.    Example 1:   Input: nums = [1,3,1,2,2] O...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt_entire = defaultdict(int)
        for c in nums:
            cnt_entire[c] += 1
        boundry = len(cnt_entire)
        cnt_sub = defaultdict(int)
        ans = 0
        l = 0
        for r, num in enumerate(nums):
            cnt_sub[num] += 1
            while len(cnt_sub) == boundry:
                cnt_sub[nums[l]] -= 1
                if cnt_sub[nums[l]] == 0:
                    del cnt_sub[nums[l]]
                l += 1
            ans += l
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2799 Count Complete Subarrays in an Array -->
