# 292. Nim Game

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math` `Brainteaser` `Game Theory`

## Problem

> You are playing the following Nim Game with your friend:   	Initially, there is a heap of stones on the table. 	You and your friend will alternate taking turns, and you go first. 	On each turn, the person whose turn it is will remove 1 to 3 stones from the heap. 	The one who removes the last stone is the winner.   Given n, the number of stones in the heap, return true if you can win the game assum...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #292 Nim Game -->
