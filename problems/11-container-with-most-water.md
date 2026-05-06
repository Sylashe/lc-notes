# 11. Container With Most Water

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Greedy`

## Problem

> You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).  Find two lines that together with the x-axis form a container, such that the container contains the most water.  Return the maximum amount of water a container can store.  Notice that you may not slant the container.    Example 1:   Input:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        ans = 0
        while l < r:
            l_h = height[l]
            r_h = height[r]
            ans = max(ans, (r - l) * min(l_h, r_h))
            if l_h < r_h:
                l += 1
            else:
                r -= 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #11 Container With Most Water -->
