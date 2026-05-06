# 125. Valid Palindrome

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Two Pointers` `String`

## Problem

> A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.  Given a string s, return true if it is a palindrome, or false otherwise.    Example 1:   Input: s = "A man, a plan, a canal: Panama" Output: true Explanation: "amanaplan...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            while l < r and (s[l] == ' ' or not s[l].isalnum()):
                l += 1
            while r > l and (s[r] == ' ' or not s[r].isalnum()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #125 Valid Palindrome -->
