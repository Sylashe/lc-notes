# 521. Longest Uncommon Subsequence I

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String`

## Problem

> Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If no such uncommon subsequence exists, return -1.  An uncommon subsequence between two strings is a string that is a subsequence of exactly one of them.    Example 1:   Input: a = "aba", b = "cdc" Output: 3 Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba"...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) > len(b):
            return len(a)
        elif len(b) > len(a):
            return len(b)
        else:
            j = 0
            for c in a:
                if c == b[j]:
                    j += 1
                if j == len(b):
                    return -1
            return len(a)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #521 Longest Uncommon Subsequence I -->
