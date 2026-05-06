# 3100. Water Bottles II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Math` `Simulation`

## Problem

> You are given two integers numBottles and numExchange.  numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:   	Drink any number of full water bottles turning them into empty bottles. 	Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.   Note that you cannot...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        BottlesDrunk = numBottles
        EmptyBottles = numBottles
        numBottles = 0
        while numExchange <= EmptyBottles:
            if numBottles > 0:
                BottlesDrunk += numBottles
                EmptyBottles += numBottles
                numBottles = 0
            BottlesDrunk += 1
            EmptyBottles -= numExchange
            EmptyBottles += 1
            numExchange += 1
        return BottlesDrunk
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3100 Water Bottles II -->
