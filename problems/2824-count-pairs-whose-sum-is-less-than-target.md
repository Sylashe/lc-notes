# 2824. Count Pairs Whose Sum is Less than Target

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers` `Binary Search` `Sorting`

## Problem

> Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.   Example 1:   Input: nums = [-1,1,2,3,1], target = 2 Output: 3 Explanation: There are 3 pairs of indices that satisfy the conditions in the statement: - (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target - (0, 2) since 0 < 2 and nums[0]...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = 0
        while l < r:
            if nums[l] + nums[r] >= target:
                r -= 1
            else:
                ans += r - l
                l += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2824 Count Pairs Whose Sum is Less than Target -->
