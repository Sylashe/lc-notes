# 922. Sort Array By Parity II

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers` `Sorting`

## Problem

> Given an array of integers nums, half of the integers in nums are odd, and the other half are even.  Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.  Return any answer array that satisfies this condition.    Example 1:   Input: nums = [4,2,5,7] Output: [4,5,2,7] Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.   Example...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = 1
        while l < n:
            if nums[l] % 2 == 0:
                l += 2
            elif nums[r] % 2 == 1:
                r += 2
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 2
                r += 2
        return nums
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #922 Sort Array By Parity II -->
