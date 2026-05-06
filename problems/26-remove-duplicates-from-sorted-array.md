# 26. Remove Duplicates from Sorted Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers`

## Problem

> Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.  Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.  The first k elements of nums should contain the unique number...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        cnt = 1
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if num != nums[i - 1]:
                nums[idx] = num
                idx += 1
                cnt += 1
        return cnt
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #26 Remove Duplicates from Sorted Array -->
