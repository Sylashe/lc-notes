# 925. Long Pressed Name

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Two Pointers` `String`

## Problem

> Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.  You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.    Example 1:   Input: name = "alex", typed = "aaleex" Output: t...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        while j < len(typed):
            if typed[j] != typed[j - 1]:
                return False
            j += 1
        return i == len(name)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #925 Long Pressed Name -->
