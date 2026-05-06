# 838. Push Dominoes

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Two Pointers` `String` `Dynamic Programming`

## Problem

> There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.  After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.  When a vertical domino has...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list("L" + dominoes + "R")
        pre_domino = 0
        for i, domino in enumerate(dominoes):
            if domino == ".":
                continue
            if domino == dominoes[pre_domino]:
                dominoes[pre_domino + 1: i] = domino * (i - pre_domino - 1)
            elif domino == "L":
                half = (i - pre_domino - 1) // 2
                dominoes[pre_domino + 1:pre_domino + half + 1] = "R" * half
                dominoes[i - half:i] = "L" * half 
            pre_domino = i
        return ''.join(dominoes[1:-1])
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #838 Push Dominoes -->
