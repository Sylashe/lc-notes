# 56. Merge Intervals

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sorting`

## Problem

> Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.    Example 1:   Input: intervals = [[1,3],[2,6],[8,10],[15,18]] Output: [[1,6],[8,10],[15,18]] Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].   Example 2:   Input: intervals =...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        ans_l = intervals[0][0]
        ans_r = intervals[0][1]
        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            cur_l = interval[0]
            cur_r = interval[1]
            if cur_l <= ans_r:
                ans_r = max(ans_r, cur_r)
            else:
                ans.append([ans_l, ans_r])
                ans_l = cur_l
                ans_r = cur_r
        ans.append([ans_l, ans_r])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #56 Merge Intervals -->
