# 278. First Bad Version

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Binary Search` `Interactive`

## Problem

> You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.  Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return r
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #278 First Bad Version -->
