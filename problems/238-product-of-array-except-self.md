# 238. Product of Array Except Self

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Prefix Sum`

## Problem

> Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.  You must write an algorithm that runs in O(n) time and without using the division operation.    Example 1: Input: nums = [1,2,3,4] Output: [24,12,8,6] Example 2: Input: num...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_s = n * [1]
        post_s = n * [1]
        ans = []
        for i in range(n - 1):
            pre_s[i + 1] = pre_s[i] * nums[i]
        for j in range(n - 2, -1, -1):
            post_s[j] = post_s[j + 1] * nums[j + 1]
        for k in range(n):
            ans.append(pre_s[k] * post_s[k])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #238 Product of Array Except Self -->
