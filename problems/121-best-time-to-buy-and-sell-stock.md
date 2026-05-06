# 121. Best Time to Buy and Sell Stock

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Dynamic Programming`

## Problem

> You are given an array prices where prices[i] is the price of a given stock on the ith day.  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.    Example 1:   Input: prices = [7,1,5,3,6,4] Output: 5 Exp...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        ans = 0
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            ans = max(price - min_price, ans)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #121 Best Time to Buy and Sell Stock -->
