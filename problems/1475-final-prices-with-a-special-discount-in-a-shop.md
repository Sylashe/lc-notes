# 1475. Final Prices With a Special Discount in a Shop

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Stack` `Monotonic Stack`

## Problem

> You are given an integer array prices where prices[i] is the price of the ith item in a shop.  There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.  Return an integer array answer where answer[i...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        non_match = []
        res = prices
        for i, price in enumerate(prices):
            while non_match and prices[non_match[-1]] >= price:
                idx = non_match.pop()
                res[idx] = prices[idx] - price
            non_match.append(i)
        return res
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1475 Final Prices With a Special Discount in a Shop -->
