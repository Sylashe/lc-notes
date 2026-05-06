# 28. Find the Index of the First Occurrence in a String

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Two Pointers` `String` `String Matching`

## Problem

> Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.    Example 1:   Input: haystack = "sadbutsad", needle = "sad" Output: 0 Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.   Example 2:   Input: haystack = "leetcode", needle = "leeto" Output: -1 Explanation: "l...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #28 Find the Index of the First Occurrence in a String -->
