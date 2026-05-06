# 344. Reverse String

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Two Pointers` `String`

## Problem

> Write a function that reverses a string. The input string is given as an array of characters s.  You must do this by modifying the input array in-place with O(1) extra memory.    Example 1: Input: s = ["h","e","l","l","o"] Output: ["o","l","l","e","h"] Example 2: Input: s = ["H","a","n","n","a","h"] Output: ["h","a","n","n","a","H"]    Constraints:   	1 <= s.length <= 105 	s[i] is a printable asci...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #344 Reverse String -->
