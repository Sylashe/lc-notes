# 1658. Minimum Operations to Reduce X to Zero

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Binary Search` `Sliding Window` `Prefix Sum`

## Problem

> You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.  Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.    Example 1:   Input: nums = [1,1,4,2,3], x = 5 Outp...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        left = 0
        ans = 0
        inner_s = s - x
        cnt_s = 0
        if s < x:
            return -1
        if s == x:
            return len(nums)
        for right, num in enumerate(nums):
            cnt_s += num
            while left < len(nums) and cnt_s > inner_s:
                cnt_s -= nums[left]
                left += 1
            if cnt_s == inner_s:
                ans = max(ans, right - left + 1)
        return len(nums) - ans if ans > 0 else -1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1658 Minimum Operations to Reduce X to Zero -->
