# 1887. Reduction Operations to Make the Array Elements Equal

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sorting`

## Problem

> Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:   	Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i. 	Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest. 	Reduce n...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        dif = 0
        ans = 0
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] != nums[i - 1]:
                dif += 1
            ans += dif
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1887 Reduction Operations to Make the Array Elements Equal -->
