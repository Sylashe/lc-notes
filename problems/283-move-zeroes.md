# 283. Move Zeroes

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers`

## Problem

> Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.  Note that you must do this in-place without making a copy of the array.    Example 1: Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0] Example 2: Input: nums = [0] Output: [0]    Constraints:   	1 <= nums.length <= 104 	-231 <= nums[i] <= 231 - 1     Follow up: Could you minimi...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_ = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[idx_], nums[i] = nums[i], nums[idx_]
                idx_ += 1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #283 Move Zeroes -->
