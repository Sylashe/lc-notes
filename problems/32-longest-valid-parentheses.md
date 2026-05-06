# 32. Longest Valid Parentheses

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `String` `Dynamic Programming` `Stack`

## Problem

> Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.    Example 1:   Input: s = "(()" Output: 2 Explanation: The longest valid parentheses substring is "()".   Example 2:   Input: s = ")()())" Output: 4 Explanation: The longest valid parentheses substring is "()()".   Example 3:   Input: s = "" Output: 0     Constrai...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        last_error = [-1]
        for i, c in enumerate(s):
            if c == '(':
                last_error.append(i)
            else:
                last_error.pop()
                if not last_error:
                    last_error.append(i)
                else:
                    ans = max(ans, i - last_error[-1])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #32 Longest Valid Parentheses -->
