# 55. Jump Game

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Dynamic Programming` `Greedy`

## Problem

> You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.  Return true if you can reach the last index, or false otherwise.    Example 1:   Input: nums = [2,3,1,1,4] Output: true Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.   Example 2:   Input: num...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            else:
                max_reach = max(max_reach, i + num)
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #55 Jump Game -->
