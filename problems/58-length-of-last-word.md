# 58. Length of Last Word

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String`

## Problem

> Given a string s consisting of words and spaces, return the length of the last word in the string.  A word is a maximal substring consisting of non-space characters only.    Example 1:   Input: s = "Hello World" Output: 5 Explanation: The last word is "World" with length 5.   Example 2:   Input: s = "   fly me   to   the moon  " Output: 4 Explanation: The last word is "moon" with length 4.   Examp...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        ans = 0
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            ans += 1
            i -= 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #58 Length of Last Word -->
