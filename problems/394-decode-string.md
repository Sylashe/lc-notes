# 394. Decode String

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Stack` `Recursion`

## Problem

> Given an encoded string, return its decoded string.  The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.  You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the orig...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        digit = 0
        res = ""
        for c in s:
            if c.isdigit():
                digit = digit * 10 + int(c)
            elif c.isalpha():
                res += c
            elif c == '[':
                numStack.append(digit)
                strStack.append(res)
                res = ""
                digit = 0
            else:
                outString = strStack.pop()
                cnt = numStack.pop()
                for _ in range(cnt):
                    outString += res
                res = outString
        return res
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #394 Decode String -->
