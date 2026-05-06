# 455. Assign Cookies

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers` `Greedy` `Sorting`

## Problem

> Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.  Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx = 0
        for cookie in s:
            if idx == len(g):
                break
            if cookie >= g[idx]:
                idx += 1
        return idx
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #455 Assign Cookies -->
