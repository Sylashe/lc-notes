# 1486. XOR Operation in an Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math` `Bit Manipulation`

## Problem

> You are given an integer n and an integer start.  Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.  Return the bitwise XOR of all elements of nums.    Example 1:   Input: n = 5, start = 0 Output: 8 Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8. Where "^" corresponds to bitwise XOR operator.   Example 2:   Input: n = 4, start =...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= (start + i * 2)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1486 XOR Operation in an Array -->
