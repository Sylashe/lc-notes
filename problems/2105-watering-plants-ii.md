# 2105. Watering Plants II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Simulation`

## Problem

> Alice and Bob want to water n plants in their garden. The plants are arranged in a row and are labeled from 0 to n - 1 from left to right where the ith plant is located at x = i.  Each plant needs a specific amount of water. Alice and Bob have a watering can each, initially full. They water the plants in the following way:   	Alice waters the plants in order from left to right, starting from the 0...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l = 0
        r = len(plants) - 1
        time = 0
        fullA = capacityA
        fullB = capacityB
        while l < r:
            if plants[l] > capacityA:
                capacityA = fullA
                time += 1
            capacityA -= plants[l]
            l += 1
            if plants[r] > capacityB:
                capacityB = fullB
                time += 1
            capacityB -= plants[r]
            r -= 1
            if l == r and max(capacityA, capacityB) < plants[l]:
                time += 1
        return time
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2105 Watering Plants II -->
