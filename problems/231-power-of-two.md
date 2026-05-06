# 231. Power of Two

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math` `Bit Manipulation` `Recursion`

## Problem

> Given an integer n, return true if it is a power of two. Otherwise, return false.  An integer n is a power of two, if there exists an integer x such that n == 2x.    Example 1:   Input: n = 1 Output: true Explanation: 20 = 1   Example 2:   Input: n = 16 Output: true Explanation: 24 = 16   Example 3:   Input: n = 3 Output: false     Constraints:   	-231 <= n <= 231 - 1     Follow up: Could you solv...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return 2**31 % n == 0
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #231 Power of Two -->
