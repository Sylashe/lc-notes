# 69. Sqrt(x)

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math` `Binary Search`

## Problem

> Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.  You must not use any built-in exponent function or operator.   	For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.     Example 1:   Input: x = 4 Output: 2 Explanation: The square root of 4 is 2, so we return 2.   Example 2:   Input: x...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l < r:
            mid = l + (r - l + 1)//2
            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1
        return l
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #69 Sqrt(x) -->
