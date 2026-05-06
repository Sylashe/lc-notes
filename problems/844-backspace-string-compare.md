# 844. Backspace String Compare

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Two Pointers` `String` `Stack` `Simulation`

## Problem

> Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.  Note that after backspacing an empty text, the text will continue empty.    Example 1:   Input: s = "ab#c", t = "ad#c" Output: true Explanation: Both s and t become "ac".   Example 2:   Input: s = "ab##", t = "c#d#" Output: true Explanation: Both s and t become ""...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 or j >= 0:
            cnt_1 = 0
            cnt_2 = 0
            while i >= 0:
                if s[i] == "#":
                    i -= 1
                    cnt_1 += 1
                elif cnt_1 > 0 and i >= 0:
                    i -= 1
                    cnt_1 -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    j -= 1
                    cnt_2 += 1
                elif cnt_2 > 0 and j >= 0:
                    j -= 1
                    cnt_2 -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #844 Backspace String Compare -->
