# 2078. Two Furthest Houses With Different Colors

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Greedy`

## Problem

> There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.  Return the maximum distance between two houses with different colors.  The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.    Example 1:   Input: c...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i, color in enumerate(colors):
            if color != colors[0]:
                ans = max(ans, i)
            if color != colors[len(colors) - 1]:
                ans = max(ans, len(colors) - i - 1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2078 Two Furthest Houses With Different Colors -->
