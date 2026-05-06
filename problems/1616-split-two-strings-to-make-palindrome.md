# 1616. Split Two Strings to Make Palindrome

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Two Pointers` `String`

## Problem

> You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.  When you split a string s into sprefix and ssuffix, eithe...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if len(a) == 1:
            return True
        def SinglePlindrome(a, b) -> bool:
            l = 0
            r = len(a) - 1
            while l < r and a[l] == b[r]:
                l += 1
                r -= 1
            preffix = a[l:r+1]
            suffix = b[l:r+1]
            return preffix == preffix[::-1] or suffix == suffix[::-1]
        return SinglePlindrome(a,b) or SinglePlindrome(b,a)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1616 Split Two Strings to Make Palindrome -->
