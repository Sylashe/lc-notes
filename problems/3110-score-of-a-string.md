# 3110. Score of a String

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String`

## Problem

> You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.  Return the score of s.    Example 1:   Input: s = "hello"  Output: 13  Explanation:  The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 11...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        gross = 0
        for i in range(0, len(s) - 1):
            gross += abs(ord(s[i]) - ord(s[i + 1]))
        return gross
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3110 Score of a String -->
