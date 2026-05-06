# 205. Isomorphic Strings

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Hash Table` `String`

## Problem

> Given two strings s and t, determine if they are isomorphic.  Two strings s and t are isomorphic if the characters in s can be replaced to get t.  All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.    Example 1:   Input: s = "egg", t = "add"  Output: tru...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp_st = dict()
        mp_ts = dict()
        for c1, c2 in zip(s, t):
            if(c1 in mp_st and mp_st[c1] != c2) or (c2 in mp_ts and mp_ts[c2] != c1):
                return False
            mp_st[c1] = c2
            mp_ts[c2] = c1
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #205 Isomorphic Strings -->
