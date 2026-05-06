# 1423. Maximum Points You Can Obtain from Cards

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sliding Window` `Prefix Sum`

## Problem

> There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.  In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.  Your score is the sum of the points of the cards you have taken.  Given the integer array cardPoints and the integer k, return the maxi...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        ans = float('+inf')
        n = len(cardPoints)
        s = 0
        for i, num in enumerate(cardPoints):
            s += num
            if i - (n - k) + 1 < 0:
                continue
            ans = min(ans, s)
            s -= cardPoints[i - (n - k) + 1]
        return sum(cardPoints) - ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1423 Maximum Points You Can Obtain from Cards -->
