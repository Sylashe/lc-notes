# 709. To Lower Case

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String`

## Problem

> Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.    Example 1:   Input: s = "Hello" Output: "hello"   Example 2:   Input: s = "here" Output: "here"   Example 3:   Input: s = "LOVELY" Output: "lovely"     Constraints:   	1 <= s.length <= 100 	s consists of printable ASCII characters.

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(0, len(s)):
            if 'A' <= s[i] <= 'Z':
                s[i] =chr(ord(s[i]) + 32)
        return ''.join(s)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #709 To Lower Case -->
