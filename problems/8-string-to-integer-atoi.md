# 8. String to Integer (atoi)

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String`

## Problem

> Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.  The algorithm for myAtoi(string s) is as follows:   	Whitespace: Ignore any leading whitespace (" "). 	Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present. 	Conversion: Read the integer by skipping leading zeros until a non-digit character...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == "-":
                sign = -1
            i += 1 
        ans = 0
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        while i < n and '0' <= s[i] <= '9':
            ans = ans * 10 + int(s[i])
            if ans > MAX:
                return MAX if sign == 1 else MIN
            i += 1
        return ans * sign
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #8 String to Integer (atoi) -->
