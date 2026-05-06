# 167. Two Sum II - Input Array Is Sorted

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Binary Search`

## Problem

> Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.  Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l + 1, r + 1]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #167 Two Sum II - Input Array Is Sorted -->
