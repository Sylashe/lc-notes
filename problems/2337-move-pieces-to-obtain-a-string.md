# 2337. Move Pieces to Obtain a String

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Two Pointers` `String`

## Problem

> You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:   	The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right. 	The character '_' represents a blank...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i = 0
        j = 0
        n = len(start)
        m = len(target)
        while i < n and j < m:
            while i < n and start[i] == "_":
                i += 1
            while j < m and target[j] == "_":
                j += 1
            if i == n and j == m:
                return True
            if i == n or j == m:
                return False
            if start[i] != target[j]:
                return False
            if start[i] == "L" and i < j:
                return False
            if start[i] == "R" and i > j:
                return False
            i += 1
            j += 1
        while i < n and start[i] == "_":
            i += 1
        while j < m and target[j] == "_":
            j += 1
        return i == n and j == m
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2337 Move Pieces to Obtain a String -->
