# 2486. Append Characters to String to Make Subsequence

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Two Pointers` `String` `Greedy`

## Problem

> You are given two strings s and t consisting of only lowercase English letters.  Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.  A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.    Example 1:   Input: s = "coaching", t =...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        n = len(s)
        m = len(t)
        while i < n and j < m:
            if j < m and s[i] == t[j]:
                j += 1
            i += 1
        return m - j
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2486 Append Characters to String to Make Subsequence -->
