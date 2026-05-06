# 392. Is Subsequence

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Two Pointers` `String` `Dynamic Programming`

## Problem

> Given two strings s and t, return true if s is a subsequence of t, or false otherwise.  A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).    Example 1: Input: s = "abc", t = "ahbgdc" Out...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        n = len(s)
        m = len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #392 Is Subsequence -->
