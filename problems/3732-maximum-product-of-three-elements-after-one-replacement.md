# 3732. Maximum Product of Three Elements After One Replacement

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Math` `Greedy` `Sorting`

## Problem

> You are given an integer array nums.  You must replace exactly one element in the array with any integer value in the range [-105, 105] (inclusive).  After performing this single replacement, determine the maximum possible product of any three elements at distinct indices from the modified array.  Return an integer denoting the maximum product achievable.    Example 1:   Input: nums = [-5,7,0]  Ou...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)
        if len(cnt) == 1:
            return nums[0] * nums[0] * 10**5
        if cnt[0] >= 2 and n == 3:
            return 0
        first_mx = 0
        first_mx_indx = -1
        for i in range(n):
            if abs(nums[i]) > abs(first_mx):
                first_mx = nums[i]
                first_mx_indx = i
        second_mx = 0
        for j in range(n):
            if abs(nums[j]) > abs(second_mx) and j != first_mx_indx:
                second_mx = nums[j]
        return abs(first_mx) * abs(second_mx) * 10 ** 5
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3732 Maximum Product of Three Elements After One Replacement -->
