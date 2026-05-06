# 1614. Maximum Nesting Depth of the Parentheses

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String` `Stack`

## Problem

> Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.    Example 1:   Input: s = "(1+(2*3)+((8)/4))+1"  Output: 3  Explanation:  Digit 8 is inside of 3 nested parentheses in the string.   Example 2:   Input: s = "(1)+((2))+(((3)))"  Output: 3  Explanation:  Digit 3 is inside of 3 nested parentheses in the string.   Example...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
                ans = max(ans, len(stack))
            if c == ')':
                stack.pop()
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1614 Maximum Nesting Depth of the Parentheses -->
