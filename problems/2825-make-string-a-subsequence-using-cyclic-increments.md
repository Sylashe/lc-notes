# 2825. Make String a Subsequence Using Cyclic Increments

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Two Pointers` `String`

## Problem

> You are given two 0-indexed strings str1 and str2.  In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.  Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.  Note:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        for c in str1:
            if c == str2[i] or chr(ord(c) + 1) == str2[i] or c == "z" and str2[i] == "a":
                i += 1
                if i == len(str2):
                    return True
        return False
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2825 Make String a Subsequence Using Cyclic Increments -->
