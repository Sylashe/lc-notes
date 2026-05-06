# 7. Reverse Integer

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Math`

## Problem

> Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.  Assume the environment does not allow you to store 64-bit integers (signed or unsigned).    Example 1:   Input: x = 123 Output: 321   Example 2:   Input: x = -123 Output: -321   Example 3:   Input: x = 120 Output: 21...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        ans = 0
        while x != 0:
            last = x % 10
            ans = ans * 10 + last
            if ans > INT_MAX or ans < INT_MIN:
                return 0
            x //= 10
        return ans * sign
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #7 Reverse Integer -->
