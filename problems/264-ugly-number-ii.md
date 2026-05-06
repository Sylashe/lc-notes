# 264. Ugly Number II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `Math` `Dynamic Programming` `Heap (Priority Queue)`

## Problem

> An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.  Given an integer n, return the nth ugly number.    Example 1:   Input: n = 10 Output: 12 Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.   Example 2:   Input: n = 1 Output: 1 Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, an...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        p2 = p3 = p5 = 0
        for i in range(1, n):
            next2, next3, next5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(next2, next3, next5)
            if dp[i] == next2:
                p2 += 1
            if dp[i] == next3:
                p3 += 1
            if dp[i] == next5:
                p5 += 1
        return dp[n-1]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #264 Ugly Number II -->
