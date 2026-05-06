# 2779. Maximum Beauty of an Array After Applying Operation

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search` `Sliding Window` `Sorting`

## Problem

> You are given a 0-indexed array nums and a non-negative integer k.  In one operation, you can do the following:   	Choose an index i that hasn't been chosen before from the range [0, nums.length - 1]. 	Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k].   The beauty of the array is the length of the longest subsequence consisting of equal elements.  Return the maximum possi...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        ans = 0
        for r,num in enumerate(nums):
            if num - nums[l] > 2 * k:
                l += 1
            ans = max(ans,r - l + 1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2779 Maximum Beauty of an Array After Applying Operation -->
