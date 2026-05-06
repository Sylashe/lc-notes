# 1124. Longest Well-Performing Interval

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Stack` `Monotonic Stack` `Prefix Sum`

## Problem

> We are given hours, a list of the number of hours worked per day for a given employee.  A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.  A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.  Return the length of the longest well-performing interval....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans = 0
        pre = 0
        first_seen = {}
        
        for i, h in enumerate(hours):
            pre += 1 if h > 8 else -1
            
            if pre > 0:
                ans = i + 1
            elif (pre - 1) in first_seen:
                ans = max(ans, i - first_seen[pre - 1])
            
            if pre not in first_seen:
                first_seen[pre] = i
        
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1124 Longest Well-Performing Interval -->
