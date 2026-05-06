# 605. Can Place Flowers

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Greedy`

## Problem

> You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.  Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.    Example 1:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        check = flowerbed[:]
        check = [0] + check + [0]
        for i in range(1, len(check) - 1):
            if check[i - 1] == 0 and check[i + 1] == 0 and check[i] == 0:
                check[i] = 1
                n -= 1
        return n <= 0
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #605 Can Place Flowers -->
