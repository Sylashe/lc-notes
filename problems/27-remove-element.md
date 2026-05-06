# 27. Remove Element

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers`

## Problem

> Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.  Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:   	Change the array nums such that the first k elements of nums...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx_ = 0
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != val:
                nums[idx_] = nums[i]
                idx_ += 1
                k += 1
        return k
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #27 Remove Element -->
