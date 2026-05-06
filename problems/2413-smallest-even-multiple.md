# 2413. Smallest Even Multiple

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math` `Number Theory`

## Problem

> Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.   Example 1:   Input: n = 5 Output: 10 Explanation: The smallest multiple of both 5 and 2 is 10.   Example 2:   Input: n = 6 Output: 6 Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.     Constraints:   	1 <= n <= 150

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2413 Smallest Even Multiple -->
