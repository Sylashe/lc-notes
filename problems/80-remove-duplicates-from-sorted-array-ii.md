# 80. Remove Duplicates from Sorted Array II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers`

## Problem

> Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.  Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        cur = nums[0]
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] == cur:
                cnt += 1
            else:
                cur = nums[i]
                cnt = 1
            if cnt <= 2:
                nums[idx] = cur
                idx += 1
        return idx
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #80 Remove Duplicates from Sorted Array II -->
