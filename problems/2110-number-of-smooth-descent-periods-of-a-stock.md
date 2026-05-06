# 2110. Number of Smooth Descent Periods of a Stock

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Math` `Two Pointers` `Dynamic Programming` `Sliding Window`

## Problem

> You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.  A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.  Return the number of smooth descent pe...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        cnt = ans = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                cnt += 1
            else:
                cnt = 1
            ans += cnt
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2110 Number of Smooth Descent Periods of a Stock -->
