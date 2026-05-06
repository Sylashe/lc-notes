# 680. Valid Palindrome II

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Two Pointers` `String` `Greedy`

## Problem

> Given a string s, return true if the s can be palindrome after deleting at most one character from it.    Example 1:   Input: s = "aba" Output: true   Example 2:   Input: s = "abca" Output: true Explanation: You could delete the character 'c'.   Example 3:   Input: s = "abc" Output: false     Constraints:   	1 <= s.length <= 105 	s consists of lowercase English letters.

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome_ij(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            if s[l] != s[r]:
                return palindrome_ij(s, l + 1, r) or palindrome_ij(s, l, r - 1)
            l += 1
            r -= 1
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #680 Valid Palindrome II -->
