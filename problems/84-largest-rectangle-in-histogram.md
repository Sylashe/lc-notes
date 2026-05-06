# 84. Largest Rectangle in Histogram

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Array` `Stack` `Monotonic Stack`

## Problem

> Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.    Example 1:   Input: heights = [2,1,5,6,2,3] Output: 10 Explanation: The above is a histogram where width of each bar is 1. The largest rectangle is shown in the red area, which has an area = 10 units.   Example 2:   Input: height...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        edge_idx = []
        new_heights = [0] + heights + [0]
        for i in range(len(new_heights)):
            while edge_idx and new_heights[i] < new_heights[edge_idx[-1]]:
                cur_idx = edge_idx.pop()
                l = edge_idx[-1]
                r = i
                cur_height = new_heights[cur_idx]
                ans = max(ans, cur_height * (r - l - 1))
            edge_idx.append(i)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #84 Largest Rectangle in Histogram -->
