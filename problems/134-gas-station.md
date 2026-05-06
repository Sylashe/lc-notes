# 134. Gas Station

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Greedy`

## Problem

> There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].  You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.  Given two integer arrays gas and cost, return the starting gas station's index if you can trav...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])
            if tank < 0:
                tank = 0
                start = i + 1
        return start
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #134 Gas Station -->
