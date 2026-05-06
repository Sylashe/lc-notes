# 326. Power of Three

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math` `Recursion`

## Problem

> Given an integer n, return true if it is a power of three. Otherwise, return false.  An integer n is a power of three, if there exists an integer x such that n == 3x.    Example 1:   Input: n = 27 Output: true Explanation: 27 = 33   Example 2:   Input: n = 0 Output: false Explanation: There is no x where 3x = 0.   Example 3:   Input: n = -1 Output: false Explanation: There is no x where 3x = (-1)....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return 3**31 % n == 0
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #326 Power of Three -->
