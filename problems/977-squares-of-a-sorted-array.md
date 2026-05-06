# 977. Squares of a Sorted Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers` `Sorting`

## Problem

> Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.    Example 1:   Input: nums = [-4,-1,0,3,10] Output: [0,1,9,16,100] Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].   Example 2:   Input: nums = [-7,-3,2,3,11] Output: [4,9,9,49,121]     Constraints:   	1...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        pos = r = len(nums) - 1
        res = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] ** 2
                l += 1
            else:
                res[pos] = nums[r] ** 2
                r -= 1
            pos -= 1
        return res
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #977 Squares of a Sorted Array -->
