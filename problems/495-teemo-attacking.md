# 495. Teemo Attacking

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Simulation`

## Problem

> Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = duration
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i - 1]
            ans += min(diff, duration)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #495 Teemo Attacking -->
