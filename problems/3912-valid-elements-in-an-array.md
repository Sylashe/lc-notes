# 3912. Valid Elements in an Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** 

## Problem

> You are given an integer array nums.  An element nums[i] is considered valid if it satisfies at least one of the following conditions:   	It is strictly greater than every element to its left. 	It is strictly greater than every element to its right.   The first and last elements are always valid.  Return an array of all valid elements in the same order as they appear in nums.    Example 1:   Input...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        pre_max = [0] * (len(nums) + 1)
        post_max = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            pre_max[i + 1] = max(pre_max[i], num)
        for i, num in enumerate(nums[::-1]):
            post_max[i + 1] = max(post_max[i], num)
        post_max = post_max[::-1]
        ans = []
        for i, num in enumerate(nums):
            if nums[i] > pre_max[i] or nums[i] > post_max[i + 1]:
                ans.append(nums[i])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3912 Valid Elements in an Array -->
