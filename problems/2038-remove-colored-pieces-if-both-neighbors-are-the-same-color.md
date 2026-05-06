# 2038. Remove Colored Pieces if Both Neighbors are the Same Color

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Math` `String` `Greedy` `Game Theory`

## Problem

> There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.  Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.   	Alice is only allowed to remove a piece colored 'A' if both its neighbors are also col...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnt_a = 0
        cnt_b = 0
        i = 0
        n = len(colors)
        while i < n:
            start_i = i
            start_color = colors[i]
            while i < n - 1 and colors[i] == colors[i+1]:
                i += 1
            if i - start_i - 1 > 0:
                if start_color == "A":
                    cnt_a += i - start_i - 1
                else:
                    cnt_b += i - start_i - 1
            i += 1
        return cnt_a > cnt_b
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2038 Remove Colored Pieces if Both Neighbors are the Same Color -->
