# 777. Swap Adjacent in LR String

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Two Pointers` `String`

## Problem

> In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string result, return True if and only if there exists a sequence of moves to transform start to result.    Example 1:   Input: start = "RXXLRXRXL", result = "XRLXX...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        i = 0
        j = 0
        n = len(start)
        m = len(result)
        while i < n and j < m:
            while i < n and start[i] == "X":
                i += 1
            while j < m and result[j] == "X":
                j += 1
            if i == n or j == m:
                break
            if start[i] != result[j]:
                return False
            if start[i] == "L" and j > i:
                return False
            if start[i] == "R" and i > j:
                return False
            i += 1
            j += 1
        while i < n and start[i] == "X":
            i += 1
        while j < m and result[j] == "X":
            j += 1
        return i == n and j == m
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #777 Swap Adjacent in LR String -->
