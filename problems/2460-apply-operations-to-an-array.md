# 2460. Apply Operations to an Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers` `Simulation`

## Problem

> You are given a 0-indexed array nums of size n consisting of non-negative integers.  You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:   	If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.   After performing all the operations, shift all...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        return nums
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2460 Apply Operations to an Array -->
