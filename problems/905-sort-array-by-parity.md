# 905. Sort Array By Parity

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers` `Sorting`

## Problem

> Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.  Return any array that satisfies this condition.    Example 1:   Input: nums = [3,1,2,4] Output: [2,4,3,1] Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.   Example 2:   Input: nums = [0] Output: [0]     Constraints:   	1 <= nums.length <= 500...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            elif nums[j] % 2 == 1:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #905 Sort Array By Parity -->
