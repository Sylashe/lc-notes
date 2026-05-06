# 137. Single Number II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Bit Manipulation`

## Problem

> Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.  You must implement a solution with a linear runtime complexity and use only constant extra space.    Example 1: Input: nums = [2,2,3,2] Output: 3 Example 2: Input: nums = [0,1,0,1,0,1,99] Output: 99    Constraints:   	1 <= nums.length <= 3 * 104 	-...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for x in cnt:
            if cnt[x] == 1:
                return x
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #137 Single Number II -->
