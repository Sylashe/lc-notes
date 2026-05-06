# 260. Single Number III

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Bit Manipulation`

## Problem

> Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.  You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.    Example 1:   Input: nums = [1,2,1,3,2,5] Output: [3,5] Explanation:  [5, 3] is also...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x
        mask = xor & -xor
        a = 0
        b = 0
        for x in nums:
            if x & mask:
                a ^= x
            else:
                b ^= x
        return [a, b]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #260 Single Number III -->
