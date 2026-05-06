# 3456. Find Special Substring of Length K

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String`

## Problem

> You are given a string s and an integer k.  Determine if there exists a substring of length exactly k in s that satisfies the following conditions:   	The substring consists of only one distinct character (e.g., "aaa" or "bbb"). 	If there is a character immediately before the substring, it must be different from the character in the substring. 	If there is a character immediately after the substri...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        cnt = 1
        for i in range(1, n):
            if s[i] != s[i - 1]:
                if cnt == k:
                    return True
                cnt = 1
            else:
                cnt += 1
        return cnt == k
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3456 Find Special Substring of Length K -->
