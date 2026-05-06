# 42. Trapping Rain Water

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Array` `Two Pointers` `Dynamic Programming` `Stack` `Monotonic Stack`

## Problem

> Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.    Example 1:   Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6 Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.   Example 2:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        pre_max = 0
        post_max = 0
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            pre_max = max(pre_max, height[l])
            post_max = max(post_max, height[r])
            if pre_max < post_max:
                ans += pre_max - height[l]
                l += 1
            else:
                ans += post_max - height[r]
                r -= 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #42 Trapping Rain Water -->
