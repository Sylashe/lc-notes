# 435. Non-overlapping Intervals

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Dynamic Programming` `Greedy` `Sorting`

## Problem

> Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.  Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.    Example 1:   Input: intervals = [[1,2],[2,3],[3,4],[1,3]] Output: 1 Explanation: [1,3] can...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        max_r = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < max_r:
                ans += 1
            else:
                max_r = max(max_r, intervals[i][1])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #435 Non-overlapping Intervals -->
