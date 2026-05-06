# 2414. Length of the Longest Alphabetical Continuous Substring

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String`

## Problem

> An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".   	For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.   Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.    Examp...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        cnt = 1
        ans = 1
        for i in range(1, len(s)):
            if s[i] == chr(ord(s[i - 1]) + 1):
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2414 Length of the Longest Alphabetical Continuous Substring -->
