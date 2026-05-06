# 1578. Minimum Time to Make Rope Colorful

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `String` `Dynamic Programming` `Greedy`

## Problem

> Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.  Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        n = len(colors)
        mx_time = 0
        totl_time = 0
        i = 0
        while i < n:
            if i < n - 1 and colors[i] != colors[i + 1]:
                i += 1
                continue
            if i < n - 1 and colors[i] == colors[i + 1]:
                color = colors[i]
                while i < n and colors[i] == color:
                    totl_time += neededTime[i]
                    mx_time = max(neededTime[i], mx_time)
                    i += 1
                ans += totl_time - mx_time
                totl_time = 0
                mx_time = 0
            else:
                i += 1
        ans += totl_time - mx_time
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1578 Minimum Time to Make Rope Colorful -->
