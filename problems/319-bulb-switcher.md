# 319. Bulb Switcher

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Math` `Brainteaser`

## Problem

> There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.  On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.  Return the number of bulbs that are on after n rounds.    Example 1:   Input: n = 3 Output:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #319 Bulb Switcher -->
