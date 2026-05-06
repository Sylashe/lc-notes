# 452. Minimum Number of Arrows to Burst Balloons

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Greedy` `Sorting`

## Problem

> There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.  Arrows can be shot up directly vertically (in the positive y-direction) from differen...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        arrow = points[0][1]
        ans = 1
        for i, point in enumerate(points):
            if point[0] > arrow:
                ans += 1
                arrow = point[1]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #452 Minimum Number of Arrows to Burst Balloons -->
