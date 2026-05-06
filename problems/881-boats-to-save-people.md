# 881. Boats to Save People

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Greedy` `Sorting`

## Problem

> You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.  Return the minimum number of boats to carry every given person.    Example 1:   Input: people = [1,2], limit = 3 Ou...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l = 0 
        r = n - 1
        ans = 0
        while l <= r:
            total = people[l] + people[r]
            if total <= limit:
                ans += 1
                l += 1
                r -= 1
            else:
                ans += 1
                r -= 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #881 Boats to Save People -->
